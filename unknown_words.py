from collections import defaultdict, Counter
from config import TAG_MAP, MAX_SUFFIX_LEN


def build_suffix_model(corpus_data):
    """ Строит модель для угадывания тега по окончанию слова для прилагательных и существительных """
    suffix_stats = defaultdict(Counter)
    for word, _, pos in corpus_data:
        tag = TAG_MAP.get(pos, "UNK")
        for length in range(1, MAX_SUFFIX_LEN + 1):
            if len(word) >= length:
                suffix = word[-length:]
                suffix_stats[suffix][tag] += 1
    suffix_model = {}
    for suffix, counter in suffix_stats.items():
        suffix_model[suffix] = counter.most_common(1)[0][0]
    return suffix_model


def guess_tag_by_suffix(word, suffix_model):
    """ Угадывает тег по известным окончаниям слова """
    for length in range(MAX_SUFFIX_LEN, 0, -1):
        if len(word) >= length:
            suffix = word[-length:]
            if suffix in suffix_model:
                return suffix_model[suffix]
    return "UNK"


def is_probable_verb(word):
    """ Проверяет, может ли слово быть глаголом по его форме """
    verb_endings = [
        "ую",
        "ла", "ло", "ли", "л",
        "ешь", "ет", "ем", "ете",
        "ишь", "ит", "им", "ите",
        "ют", "ут", "ят", "ат",
        "ю", "у",
    ]
    return any(word.endswith(ending) for ending in verb_endings)


def guess_verb_lemma(word):
    """ Угадывает лемму глагола по его форме """
    if word.endswith(("ла", "ло", "ли")):
        return word[:-2] + "ть"
    if word.endswith("л"):
        return word[:-1] + "ть"
    if word.endswith(("ешь", "ете")):
        return word[:-3] + "ть"
    if word.endswith(("ет", "ем", "ют", "ут")):
        return word[:-2] + "ть"
    if word.endswith(("ишь", "ите")):
        return word[:-3] + "ить"
    if word.endswith(("ит", "им", "ят", "ат")):
        return word[:-2] + "ить"
    if word.endswith(("аю", "яю")):
        return word[:-1] + "ть"
    if word.endswith("ую"):
        return word[:-1] + "ть"
    return word