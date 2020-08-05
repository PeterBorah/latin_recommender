with open("lingua_latina_vocab.txt") as f:
    words = [line.split()[0].replace('-', '') for line in f]
    print(words)
    print(len(words))
