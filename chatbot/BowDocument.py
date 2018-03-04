from nltk.stem.porter import *
from nltk import ngrams

'''
1: Collect all of the training dataset
2: Loop through the training data and process the queries
3: Process the queries by stemming and counting the ngrams
4: Assign the ngrams to a bag of words with a key of the classification
5: Create a dictionary with the ngrams as the key and the count as a the value
'''

class BowDocument:
    def __init__(self):
        self.tokens = []
        self.stemmer = PorterStemmer()
        self.corpus_length = 0
        self.corpus_terms = {}

    def classify(self, queries=[]):
        if len(queries) == 0:
            return

        for query in queries:
            stemmed_words = self.create_stem_words(query)
            self.create_bag_of_words(stemmed_words)

        self.process_corpus(self.tokens)

    def create_stem_words(self, words=None):
        if words is None:
            return
        return [self.stemmer.stem(word) for word in words.split()]

    def create_bag_of_words(self, stemmed_words):
        self.tokens.extend(stemmed_words)

        if len(stemmed_words) > 1:
            self.find_ngrams(stemmed_words)

        return self.tokens

    def process_corpus(self, tokens=[]):
        for stemmed_word in tokens:
            if stemmed_word not in self.corpus_terms:
                self.corpus_length += 1
                self.corpus_terms[stemmed_word] = 1
            else:
                self.corpus_length += 1
                self.corpus_terms[stemmed_word] += 1

    def find_ngrams(self, stemmed_words):
        len_of_stemmed_words = len(stemmed_words)

        if len_of_stemmed_words > 1:
            for i in range(2, 4):
                if (len_of_stemmed_words >= i):
                    self.tokens.extend([' '.join(n) for n in ngrams(stemmed_words, i)])

        return self.tokens
