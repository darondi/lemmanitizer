import re


def normalize(word):
    return word.lower().replace("ё", "е")


def tokenize(text):
    return re.findall(r"[А-Яа-яЁё]+", text)


# if __name__ == "__main__":
#     text = "Как только жизни ставишь крестик, она ставит нолик. Но если она ресторан, я занял лучший столик!"
#     print(tokenize(text))