import csv
import operator
import string

import nltk
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

import numpy as np

in_csv = csv.DictReader(open('TrumpTweets.csv', 'r', encoding='utf-8'), delimiter = ';')

def eliminate_tag(text, tag):
    ind_start = text.find(tag)
    while ind_start != -1:
        ind_end = text.find(' ', ind_start)
        if ind_end == -1:
            text = text[:ind_start]
        else:
            text = text[:ind_start] + text[ind_end:]
        ind_start = text.find(tag)
    return text

def remove_punctuations(text):
    return_text = ''
    for character in text:
        if character not in string.punctuation:
            return_text += character
    return return_text

def count_words_and_letters(text):
    word_list = text.split(' ')
    return_word_list = []
    letter_count = 0
    for word in word_list:
        if word != '':
            letter_count += len(word)
            return_word_list.append(word)
    return (return_word_list, len(return_word_list), letter_count)

def bag_of_words(tweets):
    bow = []
    for tweet in tweets:
        for word in tweet[0]:
            bow.append(word)
    return bow

def remove_stopwords(bow):
    new_bow = []
    #nltk.download('stopwords')
    stops = stopwords.words('english')
    for word in bow:
        if word not in stops:
            new_bow.append(word)
    return new_bow

def get_word_dictionary(bow):
    word_dict = {}
    for word in bow:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

def plot_top_n_words(words, n):
    x = []
    y = []
    for key, value in words[:n]:
        x.append(key)
        y.append(value)
    plt.bar(x,y)
    plt.show()
    return x

def plot_distributions_of_words(top_words, bow):
    x = np.arange(1, len(bow) + 1)
    y = np.zeros((len(top_words), len(bow)))
    for top_word_index, top_word in enumerate(top_words):
        for word_index, word in enumerate(bow):
            if top_word == word:
                y[top_word_index, word_index] = top_word_index + 1
        plt.scatter(x, y[top_word_index,:], marker= '|')
        plt.ylabel(top_words)
    plt.show()

def plot_sentiment_analysis(bow):
    #nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    concated = ''
    for word in bow:
        concated += word + ' '
    sen_scores = sid.polarity_scores(concated)
    print(sen_scores)
    values = []
    labels = []
    for key, value in sen_scores.items():
        values.append(value)
        labels.append(key)
    plt.pie(values[:-1], labels= labels[:-1], colors=['red', 'grey', 'green'], startangle=90)
    plt.show()

tweet_list = []

for tweet in in_csv:
    #print(tweet['text'])
    tweet_text = tweet['text'].lower()
    tweet_text = eliminate_tag(tweet_text, 'http')
    tweet_text = eliminate_tag(tweet_text, 'pic.')
    tweet_text = eliminate_tag(tweet_text, '@')
    tweet_text = eliminate_tag(tweet_text, '#')
    tweet_text = remove_punctuations(tweet_text)
    tweet_list.append(count_words_and_letters(tweet_text))
    #print(tweet_text)
#print(tweet_list[-10:])
bow = bag_of_words(tweet_list)
print(len(bow))
print(len(set(bow)))
print(f'Az egyedi szavak aranya: {np.round(len(set(bow)) / len(bow) * 100,2)}%')
bow = remove_stopwords(bow)
print(len(bow))
words = get_word_dictionary(bow)
#print(words)
#top_words = plot_top_n_words(words, 5)
#plot_distributions_of_words(top_words, bow)
plot_sentiment_analysis(bow)