import sys
import argparse
from trainer import train_model, train_if_needed
from model_io import load_model
from lemmatizer import lemmatize_sentence


def run_interactive():
    train_if_needed()
    dictionary, suffix_model = load_model()
    print("Введите текст:")
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print("Результат:")
            print(lemmatize_sentence(line, dictionary, suffix_model))
    except KeyboardInterrupt:
        print("\nЗавершение")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--train", action="store_true", help="обучить модель")
    parser.add_argument("-a", "--accuracy", action="store_true", help="оценить качество")
    args = parser.parse_args()
    if args.train:
        train_model()
        return
    if args.accuracy:
        from accuracy import main as run_accuracy
        run_accuracy()
        return
    run_interactive()


if __name__ == "__main__":
    main()