__author__ = 'a_medelyan'

# Goal: Learn how TextBlob performs sentiment
# https://textblob.readthedocs.org/en/dev/advanced_usage.html#advanced

from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from nltk.corpus import movie_reviews

# Two different ways of determining sentiment
blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
print blob.sentiment

blob = TextBlob("I love this library")
print blob.sentiment

# Test on new movie reviews
transcendence = ['../data/transcendence_1star.txt', '../data/transcendence_5star.txt', '../data/transcendence_8star.txt',
                 '../data/transcendence_great.txt']

# Insert code here


# Spare time? Evaluate both ways of determining sentiment.
# Also test out various polarity thresholds.

correct = 0
for fileid in movie_reviews.fileids():
    raw = movie_reviews.raw(fileid)
    blob = TextBlob(raw)
    sentiment = blob.sentiment

    guessed = 'neg'
    if sentiment.polarity > 0.11:
        guessed = 'pos'

    actual = movie_reviews.categories(fileid)[0]
    if guessed == actual:
        correct += 1

accuracy = float(correct)/len(movie_reviews.fileids())
print accuracy