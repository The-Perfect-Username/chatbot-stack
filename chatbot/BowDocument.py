import os
import math
import itertools
from nltk.stem.porter import *
import xml.etree.ElementTree as ET

class BowDocument:

    def __init__(self, classification):
        # Porter Stemmer object for stemming
        self.stemmer = PorterStemmer()
        self.classification = classification
        # Term frequency map
        self.term_freq_map = {}
        # Length of each set of queries
        self.doclen = 0
        # BM25 score
        self.bm25 = 0

    def get_freq_word_map(self):
        return self.term_freq_map

    def add_term(self, term):
        self.term_freq_map[term] = 1

    def term_count(self, term):
        term = self.stem_word_by_snowball(term)
        if term not in self.get_stop_words():
            if term in self.term_freq_map:
                self.doclen += 1
                self.term_freq_map[term] += 1
            else:
                self.doclen += 1
                self.add_term(term)

    def get_doc_len(self):
        return self.doclen

    # Stem the terms
    def stem_word_by_snowball(self, word):
        return self.stemmer.stem(word)

    def get_doc_length(self):
        return self.doclen

    def get_class(self):
        return self.classification

    def set_bm25(self, bm25):
        self.bm25 = bm25

    def get_bm25(self,):
        return self.bm25
