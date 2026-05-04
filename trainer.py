import os
from config import MODEL_PATH, TRAIN_FILES
from conllu_reader import parse_multiple
from dictionary import build_dictionary
from unknown_words import build_suffix_model
from model_io import save_model


def train_model():
    print("Запуск обучения")
    corpus_data = parse_multiple(TRAIN_FILES)
    dictionary = build_dictionary(corpus_data)
    suffix_model = build_suffix_model(corpus_data)
    save_model(dictionary, suffix_model)
    print("Обучение завершено")


def train_if_needed():
    if not os.path.exists(MODEL_PATH):
        train_model()