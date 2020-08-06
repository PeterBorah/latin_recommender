from cltk.corpus.utils.importer import CorpusImporter
from cltk.corpus.readers import get_corpus_reader
from cltk.stem.latin.declension import CollatinusDecliner
from cltk.stem.latin.j_v import JVReplacer
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer

j = JVReplacer()

with open("lingua_latina_vocab.txt") as f:
    words = [line.split()[0].
            replace('-', '').
            replace('ā', 'a').
            replace('ē', 'e').
            replace('ī', 'i').
            replace('ō', 'o').
            replace('ū', 'u')
            for line in f]
    # print(words)
    # print(len(words))

corpus_importer = CorpusImporter('latin')
# print(corpus_importer.list_corpora)

corpus_importer.import_corpus('latin_models_cltk')


lemmatizer = BackoffLatinLemmatizer()
lemmas = lemmatizer.lemmatize(words)

decliner = CollatinusDecliner()
print(decliner.decline(lemmas[40][1], flatten=True))
