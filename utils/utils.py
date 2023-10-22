import random
from nltk.corpus import PlaintextCorpusReader

def serialize_text_into_set(file: str):
    print(f"Tokenizing file {file}")
    f = open(file, "r")
    text = set(word.lower() for line in f for word in line.split() if word.isalpha())
    f.close()
    return text


def print_documents(corpus, file_names, ids):
    for id in ids:
        text = corpus.words(file_names[id])
        print('Document ID: '+str(id))
        for word in text:
            print(word,end=' ')
        print('\n')

# Splits corpus into training set and testing set
def split_class_corpus(corpus_per_classes: dict, test_fraction = 0.1):
    test_corpus = []
    train_corpus = []
    random.seed(42)
    for class_id in corpus_per_classes.keys():
        class_lst = corpus_per_classes[class_id]
        random.shuffle(class_lst)
        test_corpus_size = int(len(class_lst) * test_fraction)
        test_corpus.append(class_lst[:test_corpus_size])
        train_corpus.append(class_lst[test_corpus_size:])
    return test_corpus, train_corpus

# Reading the names of all files in the corpus
def read_corpus(corpus_root: str):
    return PlaintextCorpusReader(corpus_root, '.*\.txt')

# Listing the directories names in corpus
def list_file_names(corpus: PlaintextCorpusReader):
    return corpus.fileids()

def list_classes(corpus_dirs: [str]):
    return set([dir.split('/')[0] for dir in corpus_dirs])

def extract_words_per_classes(corpus: PlaintextCorpusReader, file_names: [], classes):
    return { c: [ corpus.words(file) for file in file_names if file.startswith(c+'/') ] for c in classes }