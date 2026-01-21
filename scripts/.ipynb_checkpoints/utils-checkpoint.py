import os
from pdbfixer import PDBFixer
from openmm.app import PDBFile
from Bio.PDB import MMCIFParser, PDBIO



def convert_cif_to_pdb(cif_file, pdb_file):
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure('model', cif_file)
    io = PDBIO()
    io.set_structure(structure)
    io.save(pdb_file)
    print(f"Saved PDB to {pdb_file}")


def fix_pdb_directory_recursive(base_dir):
    """
    Recursively fix all PDB files in base_dir and its subdirectories:
      - Adds missing residues, atoms, hydrogens
      - Generates CONECT records
      - Saves as '<original_name>.fixed.pdb' in the same directory

    Parameters:
        base_dir (str): Path to root directory containing PDB files
    """
    if not os.path.isdir(base_dir):
        raise ValueError(f"Provided path {base_dir} is not a directory!")

    print(f"Scanning directory recursively: {base_dir}")

    # Walk through all subdirectories
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(".pdb") and not file.lower().endswith(".fixed.pdb") and "cfg" not in file:
                input_path = os.path.join(root, file)
                output_path = os.path.join(root, file.replace(".pdb", ".fixed.pdb"))

                print(f"Processing: {input_path} -> {output_path}")

                try:
                    # Load the PDB
                    fixer = PDBFixer(filename=input_path)

                    # Fix the structure
                    fixer.findMissingResidues()
                    fixer.findMissingAtoms()
                    fixer.addMissingAtoms()
                    fixer.addMissingHydrogens()

                    # Write the fixed PDB
                    with open(output_path, 'w') as out_f:
                        PDBFile.writeFile(fixer.topology, fixer.positions, out_f)

                    print(f"Finished: {output_path}")
                except Exception as e:
                    print(f"Failed to process {input_path}: {e}")



def fix_single_pdb(pdb_path):
    """
    Fix a single PDB file:
      - Adds missing residues, atoms, hydrogens
      - Generates CONECT records
      - Output file: <original_name>.fixed.pdb

    Parameters:
        pdb_path (str): Path to the input PDB file
    """
    if not os.path.isfile(pdb_path):
        raise ValueError(f"Provided path {pdb_path} is not a valid file!")

    if not pdb_path.lower().endswith(".pdb"):
        raise ValueError(f"Input file must have .pdb extension: {pdb_path}")

    # Output filename
    output_path = pdb_path.replace(".pdb", ".fixed.pdb")

    print(f"Processing PDB: {pdb_path} -> {output_path}")

    try:
        # Load the PDB
        fixer = PDBFixer(filename=pdb_path)

        # Fix the structure
        fixer.findMissingResidues()
        fixer.findMissingAtoms()
        fixer.addMissingAtoms()
        fixer.addMissingHydrogens()

        # Save fixed PDB
        with open(output_path, 'w') as out_f:
            PDBFile.writeFile(fixer.topology, fixer.positions, out_f)

        print(f"Finished fixing: {output_path}")
        return output_path

    except Exception as e:
        print(f"Failed to fix {pdb_path}: {e}")
        return None
                    