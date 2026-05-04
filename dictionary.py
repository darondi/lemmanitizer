from collections import defaultdict, Counter
from config import TAG_MAP


def build_dictionary(corpus_data):
    """ Строит словарь слово: (лемма, тег). Выбирается наиболее часто встречающийся вариант """
    variants = defaultdict(Counter)
    for word, lemma, pos in corpus_data:
        tag = TAG_MAP.get(pos, "UNK")
        variants[word][(lemma, tag)] += 1
    dictionary = {}
    for word, counter in variants.items():
        best_variant = counter.most_common(1)[0][0]
        dictionary[word] = best_variant
    return dictionary
