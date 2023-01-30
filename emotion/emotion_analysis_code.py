import pandas as pd
import numpy as np
import nltk
import re
import pickle
import itertools
from nltk.stem.wordnet import WordNetLemmatizer 
from django.conf import settings
import os
import sklearn
from sklearn import svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.svm import NuSVC
from sklearn.svm import NuSVR
from sklearn.svm import LinearSVR
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer

# tweet = 'Layin n bed with a headache  ughhhh...waitin on your call...'

class emotion_analysis_code():

    lem = WordNetLemmatizer()

    def cleaning(self, text):
        txt = str(text)
        txt = re.sub(r"http\S+", "", txt)
        if len(txt) == 0:
            return 'no text'
        else:
            txt = txt.split()
            index = 0
            for j in range(len(txt)):
                if txt[j][0] == '@':
                    index = j
            txt = np.delete(txt, index)
            if len(txt) == 0:
                return 'no text'
            else:
                words = txt[0]
                for k in range(len(txt)-1):
                    words+= " " + txt[k+1]
                txt = words
                txt = re.sub(r'[^\w]', ' ', txt)
                if len(txt) == 0:
                    return 'no text'
                else:
                    txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
                    txt = txt.replace("'", "")
                    txt = nltk.tokenize.word_tokenize(txt)
                    #data.content[i] = [w for w in data.content[i] if not w in stopset]
                    for j in range(len(txt)):
                        txt[j] = self.lem.lemmatize(txt[j], "v")
                    if len(txt) == 0:
                        return 'no text'
                    else:
                        return txt

    def predict_emotion(self, tweet):

        tweet_in_pandas = pd.Series(' '.join(self.cleaning(tweet)))

        path_vec = os.path.join(settings.MODELS, 'vectorizer.pickle')
        path_model = os.path.join(settings.MODELS, 'finalized_model.sav')

        # load vectorizer
        # vec_file = 'vectorizer.pickle'
        vectorizer = pickle.load(open(path_vec, 'rb'))

        # load trained model
        # filename = 'finalized_model.sav'
        model = pickle.load(open(path_model, 'rb'))




        test = vectorizer.transform(tweet_in_pandas)
        predicted_sentiment = model.predict(test)
        final_sentiment = (predicted_sentiment[0])
        if final_sentiment == 'worry':
            return 'Worry'
        elif final_sentiment == 'sadness':
            return 'Sadness'
        elif final_sentiment == 'happiness':
            return 'Happiness'
        elif final_sentiment == 'love':
            return 'Love'
        elif final_sentiment == 'hate':
            return 'Hate'