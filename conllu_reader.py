from tokenizer import normalize


def parse_conllu(filepath):
    """ Парсер .conllu файла для получения списка в формате (слово, лемма, часть речи) """
    data = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            token_id = parts[0]
            if not token_id.isdigit():
                continue
            form = normalize(parts[1])
            lemma = normalize(parts[2])
            upos = parts[3]
            if not form.isalpha():
                continue
            data.append((form, lemma, upos))
    return data


def parse_multiple(filepaths):
    all_data = []
    for filepath in filepaths:
        data = parse_conllu(filepath)
        all_data.extend(data)
    return all_data
