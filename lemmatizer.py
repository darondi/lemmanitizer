from tokenizer import tokenize, normalize
from unknown_words import is_probable_verb, guess_verb_lemma, guess_tag_by_suffix

SPECIAL_WORDS = {
    "никуда": ("никуда", "NI"),
    "никогда": ("никогда", "NI"),
    "никто": ("никто", "NI"),
    "ничто": ("ничто", "NI"),
    "некуда": ("некуда", "NI"),
    "некого": ("некого", "NI"),
    "гришины": ("гришин", "A"),
}


def guess_lemma(word, tag):
    """ Угадывает лемму по слову и тегу (для прилагательных и существительных по известным окончаниям) """
    if tag == "V":
        return guess_verb_lemma(word)
    if tag == "A":
        endings = {
            "ая": "ый",
            "яя": "ий",
            "ое": "ый",
            "ее": "ий",
            "ого": "ый",
            "его": "ий",
            "ому": "ый",
            "ему": "ий",
            "ыми": "ый",
            "ими": "ий",
            "ой": "ый",
            "ый": "ый",
            "ий": "ий",
        }
        for ending, lemma_ending in endings.items():
            if word.endswith(ending):
                return word[:-len(ending)] + lemma_ending
    if tag == "S":
        endings = {
            "ами": "а",
            "ями": "я",
            "ах": "",
            "ях": "я",
            "ов": "",
            "ев": "",
            "ей": "",
            "ом": "",
            "ем": "",
            "ой": "а",
            "ы": "а",
            "и": "а",
        }
        for ending, lemma_ending in endings.items():
            if word.endswith(ending) and len(word) > len(ending):
                return word[:-len(ending)] + lemma_ending
    return word


def lemmatize_word(token, dictionary, suffix_model):
    """ Обрабатывает одно слово"""
    word = normalize(token)
    if word in SPECIAL_WORDS:
        lemma, tag = SPECIAL_WORDS[word]
        return f"{token}{{{lemma}={tag}}}"
    if word in dictionary:
        lemma, tag = dictionary[word]
        return f"{token}{{{lemma}={tag}}}"
    if is_probable_verb(word):
        lemma = guess_verb_lemma(word)
        return f"{token}{{{lemma}=V}}"
    tag = guess_tag_by_suffix(word, suffix_model)
    lemma = guess_lemma(word, tag)
    return f"{token}{{{lemma}={tag}}}"


def lemmatize_sentence(sentence, dictionary, suffix_model):
    """ Обрабатывает предложение """
    tokens = tokenize(sentence)
    result = []
    for token in tokens:
        result.append(lemmatize_word(token, dictionary, suffix_model))
    return " ".join(result)