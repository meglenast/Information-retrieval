import json

from nltk.corpus import PlaintextCorpusReader
from typing import List

from .utils import serialize_text_into_set
from .logger import Logger

class ReverseIndex:
    def __init__(self, source):
        if type(source) is list:
            self.build_r_index_from_files(source)
        elif type(source) is str:
            self.build_r_index_from_corpus(source)
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
        self.ri = ri

    def build_r_index_from_corpus(self, corpus_path):
        Logger.info("Building reverse index from corpus")
        self.corpus = PlaintextCorpusReader(corpus_path, '.*\.txt')
        self.files = [ f"{corpus_path}/" + file for file in self.corpus.fileids()]
        self.build_r_index_from_files(self.files)

    def lst1_and_lst2_by_terms(self, term1: str, term2: str):
        lst1 = self.ri.get(term1)
        lst2 = self.ri.get(term2)

        return self.lst1_and_lst2(lst1, lst2)

    def lst1_and_lst2(self, lst1, lst2):
        ptr1 = ptr2 = 0
        result = []

        while ptr1 < len(lst1) and ptr2 < len(lst2):
            if lst1[ptr1] == lst2[ptr2]:
                result.append(lst1[ptr1])
                ptr1 +=1
                ptr2 +=1
            elif lst1[ptr1] < lst2[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1
        return result

    def lst1_or_lst2_by_terms(self, term1: str, term2: str):
        lst1 = self.ri.get(term1)
        lst2 = self.ri.get(term2)

        return self.lst1_or_lst2(lst1, lst2)

    def lst1_or_lst2(self, lst1, lst2):
        ptr1 = ptr2 = 0
        result = []

        while ptr1 < len(lst1) or ptr2 < len(lst2):
            if ptr1 == len(lst1) or (ptr2 < len(lst2) and lst2[ptr2] < lst1[ptr1]):
                result.append(lst2[ptr2])
                ptr2 += 1
            elif ptr2 == len(lst2) or (ptr1 < len(lst1) and lst1[ptr1] < lst2[ptr2]):
                result.append(lst1[ptr1])
                ptr1 += 1
            else:
                result.append(lst1[ptr1])
                ptr1 += 1
                ptr2 += 1
        return result

    def lst1_and_not_lst2_by_terms(self, term1: str, term2: str):
        lst1 = self.ri.get(term1)
        lst2 = self.ri.get(term2)

        return self.lst1_and_not_lst2(lst1, lst2)

    def lst1_and_not_lst2(self, lst1, lst2):
        ptr1 = ptr2 = 0
        result = []

        while ptr1 < len(lst1) and ptr2 < len(lst2):
            if lst1[ptr1] == lst2[ptr2]:
                ptr1 +=1
                ptr2 +=1
            elif lst1[ptr1] < lst2[ptr2]:
                result.append(lst1[ptr1])
                ptr1 += 1
            else:
                ptr2 += 1

        while ptr1 < len(lst1):
            result.append(lst1[ptr1])
            ptr1 += 1
        return result

    def lst1_or_not_lst2_by_terms(self, term1: str, term2: str):
        lst1 = self.ri.get(term1)
        lst2 = self.ri.get(term2)

        return self.lst1_or_not_lst2(lst1, lst2)

    def lst1_or_not_lst2(self, lst1, lst2):
        result = set(lst1);
        ri_size = len(self.ri)

        for i in range(0,ri_size):
            if i not in lst2:
                result.add(i)

        return list(result)

    def serialize_to_txt(self, file_name: str):
        with open(file_name, "w") as f:
            for key, value in self.ri.items():
                f.write("%s:%s\n" % (key, value))

    def display(self):
        print(self.ri)