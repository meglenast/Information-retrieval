"""Build reverse index from a list of .txt files.

Usage:
  build_reverse_index.py -f [FILE ...]
  build_reverse_index.py ship -d <directory>
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
    r = RI.ReverseIndex(files)
    