import numpy as np
import pickle
import os
from typing import List, Tuple, Dict

def load_models(path: str) -> dict:
    '''
    Load machine learning models from pickle files in the specified directory.

    Args:
        path (str):
            The directory path where the pickle files of the machine learning models are stored.

    Returns:
        dict:
            A dictionary containing the loaded machine learning models,
            where the keys are model names (extracted from the filenames)
            and the values are the corresponding loaded models.
    '''

    model_dict = {}

    # List all files in the current directory
    models_in_current_directory = os.listdir(path)

    # Filter out directories from the list (exclude subdirectories)
    model_ls = [model_file for model_file in models_in_current_directory]
    
    for model_file in model_ls:
        with open(path+model_file, 'rb') as file:
            model = pickle.load(file)
        model_name = model_file.split('.')[0]
        model_dict[model_name] = model

    return model_dict




