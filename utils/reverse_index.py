from nltk.corpus import PlaintextCorpusReader
from typing import List

from .utils import serialize_text_into_set
from .logger import Logger

class ReverseIndex:
    def __init__(self, source):
        if type(source) is list:
            self.r_idex = self.build_r_index_from_files(source)
        elif type(source) is str:
            self.r_idex = self.build_r_index_from_corpus(source)
        else:
            Logger.error("Invalid source to build reverse index from.")
            raise TypeError("[Error]: Invalid source to build reverse index from.")

    def build_r_index_from_files(self, files: List[str]):
        Logger.info("Building reverse index from files list")

        ri = {}
        for idx, file in enumerate(files):
            words = serialize_text_into_set(file)
            for word in words:
                if word not in ri:
                    ri[word] = [idx]
                else:
                    (ri[word]).append(idx)

        print(ri)

    def build_r_index_from_corpus(self, corpus_path):
        Logger.info("Building reverse index from corpus")
        corpus = PlaintextCorpusReader(corpus_path, '.*\.txt')
        files = [ f"{corpus_path}/" + file for file in corpus.fileids()]

        ri = self.build_r_index_from_files(files)