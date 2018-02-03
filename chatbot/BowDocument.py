import os
import math
import itertools
from nltk.stem.porter import *
import xml.etree.ElementTree as ET

class BowDocument:

    def __init__(self):
        self.stemmer = PorterStemmer()

    def start(self):
        user_input = input()

        words = [self.stemmer.stem(i) for i in user_input.split(' ')]

        print(words)

BD = BowDocument()

BD.start()
