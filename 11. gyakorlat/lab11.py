import csv
import string

import nltk
from nltk.corpus import stopwords

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
    nltk.download('stopwords')
    for word in bow:
        if word not in stopwords.words('english'):
            new_bow.append(word)
    return new_bow

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