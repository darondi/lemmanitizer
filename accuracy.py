import os
from config import MODEL_PATH, TEST_FILE, TAG_MAP
from trainer import train_if_needed
from conllu_reader import parse_conllu
from model_io import load_model
from lemmatizer import lemmatize_word


def main():
    """ Оценивает точность модели на тестовом наборе данных """
    if not os.path.exists(MODEL_PATH):
        train_if_needed()
    print("Загрузка модели")
    dictionary, suffix_model = load_model()
    print("Загрузка тестовых данных")
    test_data = parse_conllu(TEST_FILE)
    total = 0
    correct_lemma = 0
    correct_tag = 0
    correct_full = 0
    for word, gold_lemma, gold_pos in test_data:
        gold_tag = TAG_MAP.get(gold_pos, "UNK")
        result = lemmatize_word(word, dictionary, suffix_model)
        inside = result.split("{", 1)[1].rstrip("}")
        predicted_lemma, predicted_tag = inside.split("=", 1)
        total += 1
        if predicted_lemma == gold_lemma:
            correct_lemma += 1
        if predicted_tag == gold_tag:
            correct_tag += 1
        if predicted_lemma == gold_lemma and predicted_tag == gold_tag:
            correct_full += 1
    print("Всего слов:", total)
    print("Точность лемм:", round(correct_lemma / total, 4))
    print("Точность тегов:", round(correct_tag / total, 4))
    print("Полная точность:", round(correct_full / total, 4))


if __name__ == "__main__":
    main()