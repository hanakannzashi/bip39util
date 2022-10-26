bip39_words = [e.strip() for e in open("./bip39.txt", "r")]


def match_bip39_words(prefix: str) -> list:
    return [e for e in bip39_words if e.startswith(prefix.lower())]


if __name__ == "__main__":
    while True:
        print(match_bip39_words(input()))
