import os

BASE_DIR = os.path.dirname(__file__)

DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")

TRAIN_FILES = [
    os.path.join(DATA_DIR, "ru_syntagrus-ud-train-a.conllu"),
    os.path.join(DATA_DIR, "ru_syntagrus-ud-train-b.conllu"),
    os.path.join(DATA_DIR, "ru_syntagrus-ud-train-c.conllu"),
]

TEST_FILE = os.path.join(DATA_DIR, "ru_syntagrus-ud-test.conllu")

MODEL_PATH = os.path.join(MODELS_DIR, "model.pkl")

TAG_MAP = {
    "NOUN": "S", # существительное
    "PROPN": "S", # имя собственное
    "ADJ": "A", # прилагательное
    "VERB": "V", # глагол
    "AUX": "V", # вспомогательный глагол
    "ADV": "ADV", # наречие
    "ADP": "PR", # предлог
    "CCONJ": "CONJ", # сочинительный союз
    "SCONJ": "CONJ", # подчинительный союз
    "PRON": "NI", # местоимение
    "DET": "NI", # местоименное слово
    "NUM": "NI", # числительное
    "PART": "ADV", # частица
    "INTJ": "UNK", # междометие
    "X": "UNK", # неизвестная часть речи
}

MAX_SUFFIX_LEN = 4