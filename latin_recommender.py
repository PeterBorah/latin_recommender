from cltk.corpus.utils.importer import CorpusImporter
from cltk.corpus.readers import get_corpus_reader
from cltk.stem.latin.declension import CollatinusDecliner
from cltk.stem.latin.j_v import JVReplacer
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer

j = JVReplacer()

def get_methods(some_object):
    print([method_name for method_name in dir(some_object)
            if callable(getattr(some_object, method_name))])

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
print(corpus_importer.list_corpora)

corpus_importer.import_corpus('latin_models_cltk')

# lemmatizer = BackoffLatinLemmatizer()
# lemmas = lemmatizer.lemmatize(words)

# decliner = CollatinusDecliner()
# print(decliner.decline(lemmas[40][1], flatten=True))

corpus_importer.import_corpus("latin_text_perseus")
reader = get_corpus_reader(language='latin', corpus_name="latin_text_perseus")
docs = list(reader.docs())
print("perseus:", len(docs))

corpus_importer.import_corpus("latin_text_latin_library")
reader = get_corpus_reader(language='latin', corpus_name="latin_text_latin_library")
docs = list(reader.docs())
print("latin library:", len(docs))

corpus_importer.import_corpus("latin_text_tesserae")
reader = get_corpus_reader(language='latin', corpus_name="latin_text_tesserae")
# print(get_methods(reader))
print("tesserae:", len(reader.fileids()))
# print(reader.raw('texts/valerius_flaccus.argonautica.part.4.tess'))
