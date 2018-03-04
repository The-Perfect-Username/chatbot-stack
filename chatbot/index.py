
from nltk.stem.porter import *
from nltk import ngrams
import re
from BowDocument import BowDocument

from TrainingData import training_data
from TrainingSet import TrainingSet

response_messages = {}
context_messages = {}
classifier = {}

for data in training_data:
    queries = training_data[data]['queries']
    B = BowDocument()
    B.classify(queries=queries)
    classifier[data] = {
        'corpus_terms': B.corpus_terms,
        'corpus_length': B.corpus_length
        }


query = "Can you deliver to my location?"
Query = BowDocument()
Query.classify(queries=[query])
query = Query.corpus_terms


for classification_label in classifier:
    if classifier[classification_label]['corpus_length'] > 0:
        print (classification_label)
        TS = TrainingSet()
        print(TS.start(classification_label=classification_label, training_data=classifier, stemmed_query_terms=query))

# stemmer = PorterStemmer()
# classes = list(set(next(iter(data)) for data in training_data))
#
# def set_classifications(classes):
#     for c in classes:
#         class_words[c] = []
#
# def set_context(context, classification):
#     if context in context_messages:
#         context_messages[context].append(classification)
#     else:
#         context_messages[context] = [classification]
#
# def process_corpus(tokens=[], classification=None, data_body={}):
#     for stemmed_word in tokens:
#         if stemmed_word not in corpus_words:
#             corpus_words[stemmed_word] = 1
#         else:
#             corpus_words[stemmed_word] += 1
#
#         class_words[classification].extend([stemmed_word])
#         # response_messages[classification] = data_body['response']
#
# def create_stem_words(words):
#     return [stemmer.stem(word) for word in words.split()]
#
# def process_data(training_data):
#     for data in training_data:
#         classification = next(iter(data))
#
#         data_body = data[classification]
#         tokens = []
#
#         queries = [re.sub('[!?]', '', query) for query in data_body['queries']]
#
#         for query in queries:
#
#             stemmed_words = create_stem_words(query)
#
#             tokens.extend(stemmed_words)
#             len_of_stemmed_words = len(stemmed_words)
#
#             if len_of_stemmed_words > 1:
#                 for i in range(2, 4):
#                     if (len_of_stemmed_words >= i):
#                         tokens.extend([' '.join(n) for n in ngrams(stemmed_words, i)])
#
#         process_corpus(tokens=tokens, classification=classification, data_body=data_body)
#
#         if 'context' in data_body:
#             set_context(data_body['context'], classification)
#
# set_classifications(classes)
# process_data(training_data)
#
# user_input = None
# dictionaries = {}
# set_class = None
#
# print ("Hello, I am a chatbot designed to help you answer questions about payment. Please feel free to ask me anything payment related")
#
# for d in training_data:
#     dictionaries.update(d)
#
# while user_input is not 'Exit':
#
#     user_input = input()
#
#     if set_class is not None:
#
#         if type(set_class) is str:
#             response = dictionaries[set_class]['response']
#
#             if 'next_class' in dictionaries[set_class]:
#                 set_class = dictionaries[set_class]['next_class']
#             else:
#                 set_class = None
#
#             if (callable(response)):
#                 print(response(user_input=user_input))
#             else:
#                 print(response)
#         else:
#
#             if user_input is not "" and user_input is not None:
#                 score = 0
#
#                 user_query = [stemmer.stem(word) for word in re.sub('[!?]', '', user_input).split()]
#                 stemmed_words = user_query
#
#                 len_of_stemmed_words = len(user_query)
#
#                 if len_of_stemmed_words > 1:
#                     for i in range(2, 4):
#                         if (len_of_stemmed_words >= i):
#                             stemmed_words.extend([' '.join(n) for n in ngrams(user_query, i)])
#
#                 responses = {}
#                 set_class_words = {}
#                 for sc in set_class:
#                     set_class_words[sc] = class_words[sc]
#
#                 for stemmed_word in stemmed_words:
#                     for classes in set_class_words:
#                         if stemmed_word in set_class_words[classes]:
#                             score += (1 / corpus_words[stemmed_word])
#                             if classes not in responses:
#                                 responses[classes] = score
#                             else:
#                                 responses[classes] += score
#
#                 sorted_responses = sorted(responses.items(), key=lambda x:x[1], reverse=True)
#
#                 if len(sorted_responses) > 0:
#
#                     classification = sorted_responses[0][0]
#                     classification_score = sorted_responses[0][1]
#                     response = dictionaries[classification]['response']
#
#                     if 'next_class' in dictionaries[classification]:
#                         set_class = dictionaries[classification]['next_class']
#                     else:
#                         set_class = None
#
#                     if (callable(response)):
#                         response(user_input=user_input)
#                     else:
#                         print(response)
#                 else:
#                     print("I'm sorry, I don't fully understand what you mean")
#
#     else:
#         if user_input is not "" and user_input is not None:
#             score = 0
#
#             user_query = [stemmer.stem(word) for word in re.sub('[!?]', '', user_input).split()]
#             stemmed_words = user_query
#
#             len_of_stemmed_words = len(user_query)
#
#             if len_of_stemmed_words > 1:
#                 for i in range(2, 4):
#                     if (len_of_stemmed_words >= i):
#                         stemmed_words.extend([' '.join(n) for n in ngrams(user_query, i)])
#
#             responses = {}
#
#             for stemmed_word in stemmed_words:
#                 for classes in class_words:
#                     if stemmed_word in class_words[classes]:
#                         score += (1 / corpus_words[stemmed_word])
#                         if classes not in responses:
#                             responses[classes] = score
#                         else:
#                             responses[classes] += score
#
#             sorted_responses = sorted(responses.items(), key=lambda x:x[1], reverse=True)
#
#             if len(sorted_responses) > 0:
#
#                 classification = sorted_responses[0][0]
#                 classification_score = sorted_responses[0][1]
#                 response = dictionaries[classification]['response']
#
#                 if 'next_class' in dictionaries[classification]:
#                     set_class = dictionaries[classification]['next_class']
#                 else:
#                     set_class = None
#
#                 if (callable(response)):
#                     response(user_input=user_input)
#                 else:
#                     print(response)
#             else:
#                 print("I'm sorry, I don't fully understand what you mean")
