import math

class TrainingSet:

    def __init__(self):
        self.stemmed_query_terms = []
        self.corpus = {}
        self.training_data = {}
        self.total_len_avg = 0
        self.corpus_length = 0
        self.classification_label = None

    def start(self, classification_label=None, training_data={}, stemmed_query_terms=[]):

        if classification_label is None:
            print("Error: No classification label was found")
            return

        self.classification_label = classification_label

        len_of_training_data_set = len(training_data)

        if len_of_training_data_set == 0:
            print("Error: Training data set is empty")
            return

        if len(stemmed_query_terms) == 0:
            print("Error: Query cannot be left blank")
            return

        self.stemmed_query_terms = stemmed_query_terms
        self.training_data = training_data
        self.total_len_avg = self.get_doc_len_avg(classification_label)

        shared_corpus_terms = {}

        for ngram in ['unigrams', 'bigrams', 'trigrams']:
            shared_corpus_terms[ngram] = self.count_shared_terms(ngram)

        return shared_corpus_terms

    def get_doc_len_avg(self, classification_label):
        return self.training_data[classification_label]['corpus_length'] / len(self.training_data)

    #     __f__ = self.corpus[term] if term in self.corpus else 0.0
    #     __qf__ = self.stemmed_query_terms[term] if term in self.stemmed_query_terms else 0.0
    #     # Number of documents containing query term
    #     __n__ = shared_terms[term] if term in shared_terms else 0.0
    #
    #
    #     print("__n__ {}".format(__n__))
    #     print("__r__ {}".format(__r__))
    #
    #     part1 = ( __r__ + 0.5 ) / ( __R__ - __r__ + 0.5 )
    #     part2 = ( __n__ - __r__ + 0.5 ) / ( __N__ - __n__ - __R__ + __r__ + 0.5 )
    #     part3 = (((self.k1 + 1 ) * __f__ ) / ( __K__ + __f__ ))
    #     part4 = (((self.k2 + 1) * __qf__ ) / ( self.k2 + __qf__ ))
    #     #
    #     # print("part1 {}".format(part1))
    #     # print("part2 {}".format(part2))
    #     # print("part3 {}".format(part3))
    #     # print("part4 {}".format(part4))
    #
    #     alg = math.log(part1 / part2) * part3 * part4
    #
    #     sum_of_bm25 += alg
    #
    # # print('\n')
    # return sum_of_bm25

    ## Records the terms that are shared across several documents
    ## in the same dictionary
    def count_shared_terms(self, ngram):
        # New dictionary to be created then sorted
        shared_corpus_terms = {}
        # Dictionary of all frequent words
        self.corpus = self.training_data[self.classification_label]['corpus_terms']

        for td_classification_label, corpus_data in self.training_data.items():

            if td_classification_label != self.classification_label:

                current_corpus = self.training_data[td_classification_label]['corpus_terms']

                for token in current_corpus[ngram]:
                    # If the token exists, count by 1
                    if token in self.corpus[ngram]:
                        shared_corpus_terms[token] += 1
                    else: # Add the token to the new dictionary
                        shared_corpus_terms[token] = 1
        # Sort the dictionary by the number of tokens and return the sorted dictionary
        return dict(self.sort_dict(shared_corpus_terms))

    def sort_dict(self, dictionary):
        return sorted(dictionary.items(), key=lambda x:x[1], reverse=True)
