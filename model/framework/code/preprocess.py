import pandas as pd
import datamol as dm

def _preprocess(smile):
    mol = dm.to_mol(smile, ordered=True)
    mol = dm.fix_mol(mol)
    mol = dm.sanitize_mol(mol, sanifix=True, charge_neutral=False)
    mol = dm.standardize_mol(
        mol,
        disconnect_metals=False,
        normalize=True,
        reionize=True,
        uncharge=False,
        stereo=True,
    )
    
    return mol


def get_standard_smiles(mol):
    return dm.standardize_smiles(dm.to_smiles(mol))

def get_selfies_smiles(mol):
    return dm.to_selfies(mol)

def get_inchi_smile(mol):
    return dm.to_inchi(mol)

def get_inchi_key(mol):
    return dm.to_inchikey(mol)