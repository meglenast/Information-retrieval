"""Build reverse index from a list of .txt files.

Usage:
  build_reverse_index.py -f [FILE ...] -o <output_file>
  build_reverse_index.py -c <corpus> -o <output_file>
  build_reverse_index.py (-h | --help)

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt

from utils import reverse_index as RI
from utils import trie as T
from utils import utils
from nltk.corpus import PlaintextCorpusReader

if __name__ == '__main__':
    arguments = docopt(__doc__)
    files = arguments['FILE']
    corpus_root = arguments['<corpus>']
    output_file = arguments['<output_file>']

    # r = RI.ReverseIndex(files) if files != [] else RI.ReverseIndex(corpus)
    # trie = T.Trie()
    # trie.add_word('megie')
    # trie.display()
    
    corpus = PlaintextCorpusReader(corpus_root, '.*\.txt')
    fileNames = corpus.fileids()
    classesSet = set( [ file[:file.find('/')] for file in fileNames ] )
    classes = sorted(list(classesSet - {'Z','D-Society'}))

    print(classes)

    fullClassCorpus = [ [ corpus.words(file) for file in fileNames if file.find(c+'/')==0 ] for c in classes ]
    print(fullClassCorpus[0][0][14])