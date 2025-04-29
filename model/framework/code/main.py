import os
import csv
import sys
import pandas as pd
import datamol as dm
from preprocess import _preprocess, get_standard_smiles,get_selfies_smiles,get_inchi_key,get_inchi_smile

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

def my_model(smiles_list):

    list_standar_smile=[]
    list_selfie_smile=[]
    list_inchi_smile=[]
    list_inchi_key_smile=[]

    for smi in smiles_list:
       rmol= _preprocess(smi) 
       list_standar_smile.append(get_standard_smiles(rmol)) #get the smiles standard 
       list_selfie_smile.append(get_selfies_smiles(rmol)) #get the selfies
       list_inchi_smile.append(get_inchi_smile(rmol)) #get the inchi
       list_inchi_key_smile.append(get_inchi_key(rmol)) #get the inchi_key
    
    dict={'standard_smiles':list_standar_smile, 'selfie': list_selfie_smile, 'inchi':list_inchi_smile, 'inchikey': list_inchi_key_smile}
    df=pd.DataFrame(dict)
    #write in .csv 
    df.to_csv(output_file, index=False)
    
# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]

# run model
my_model(smiles_list)
