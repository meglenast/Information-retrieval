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
if __name__ == '__main__':
    arguments = docopt(__doc__)
    files = arguments['FILE']
    corpus = arguments['<corpus>']
    output_file = arguments['<output_file>']

    r = RI.ReverseIndex(files) if files != [] else RI.ReverseIndex(corpus)

    print(res)