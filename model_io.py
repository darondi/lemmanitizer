import os
import pickle
from config import MODEL_PATH, MODELS_DIR


def save_model(dictionary, suffix_model, filepath=MODEL_PATH):
    os.makedirs(MODELS_DIR, exist_ok=True)
    model = {
        "dictionary": dictionary,
        "suffix_model": suffix_model,
    }
    with open(filepath, "wb") as file:
        pickle.dump(model, file)


def load_model(filepath=MODEL_PATH):
    with open(filepath, "rb") as file:
        model = pickle.load(file)
    return model["dictionary"], model["suffix_model"]