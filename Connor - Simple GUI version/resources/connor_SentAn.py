from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from colorama import Fore

stopwords = nltk.corpus.stopwords.words('english')
sia = SentimentIntensityAnalyzer()


class Sentiment:
    def __init__(self, sentence):
        self.sentence = sentence
        self.score = 0

    def sentiment_analysis(self):
        self.tokenized = nltk.word_tokenize(self.sentence)
        self.tokenized = [w for w in self.tokenized if w.isalpha() and w not in stopwords]
        self.tokenized = " ".join(self.tokenized)
        analysis = sia.polarity_scores(self.tokenized)
        self.score = analysis['compound']


