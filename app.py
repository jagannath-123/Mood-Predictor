import nltk
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer, WordNetLemmatizer

class MoodPredictor:
    def __init__(self):
        self.stopword = nltk.corpus.stopwords.words('english')
        self.stemmer = PorterStemmer()
        self.bag_of_words = pickle.load(open("bag_of_words.sav","rb"))

        self.model=pickle.load(open("model.sav","rb"))
    
    def predict(self, text):
        text = new_sample = self.bag_of_words.transform(pd.Series( ' '.join([self.stemmer.stem(i.lower()) for i in text.split() if i.isalpha() and i.lower() not in self.stopword] if type(text)==str else []) )).toarray()
        result = self.model.predict(text)[0]
        return f"you are {result}"

        
        


