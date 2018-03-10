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
        self.tokens = {'unigrams': [], 'bigrams': [], 'trigrams': []}
        self.stemmer = PorterStemmer()
        self.corpus_length = 0
        self.corpus_terms = {'unigrams': {}, 'bigrams': {}, 'trigrams': {}}
        self.ngrams = {'1': 'unigrams', '2': 'bigrams', '3': 'trigrams'}

    def classify(self, queries=[]):
        if len(queries) == 0:
            return

        for query in queries:
            stemmed_words = self.create_stem_words(query)
            self.corpus_length += len(stemmed_words)
            self.create_bag_of_words(stemmed_words)

        self.process_corpus(self.tokens)

    def create_stem_words(self, words=None):
        if words is None:
            return
        return [self.stemmer.stem(word) for word in words.split()]

    def create_bag_of_words(self, stemmed_words):
        self.tokens['unigrams'].extend(stemmed_words)

        if len(stemmed_words) > 1:
            self.find_ngrams(stemmed_words)

        return self.tokens

    def process_corpus(self, tokens={}):
        for ngram in tokens:
            for stemmed_word in tokens[ngram]:
                if stemmed_word not in self.corpus_terms[ngram]:
                    self.corpus_terms[ngram][stemmed_word] = 1
                else:
                    self.corpus_terms[ngram][stemmed_word] += 1

    def find_ngrams(self, stemmed_words):
        len_of_stemmed_words = len(stemmed_words)
        if len_of_stemmed_words > 1:
            for i in range(2, 4):
                if (len_of_stemmed_words >= i):
                    self.tokens[self.ngrams[str(i)]].extend([' '.join(n) for n in ngrams(stemmed_words, i)])

        return self.tokens
