import sys
import json
from collections import defaultdict
import re

def create_sentiment(f_sentiment):
    """
    Generates sentiment dictionary
    f_sentiment: file handle
    """
    sent = {}
    for line in f_sentiment:
        values = line.rstrip().split('\t')
        sent[values[0]] = float(values[1])
    return sent

def output_term_sentiment(tweet_file, sent_amounts):
    """
    Output sentiment for all words not in sentiment amounts.

    Compute the sentiment of other words by computing sentiment sum of
    all sentiment words.

    tweet_file: file handle of tweet
    sent_amounts: dictionary of sentiment scores

    Return: term sentiment
    """
    term_sentiment = defaultdict(list)
    for tweet in tweet_file:
        try:
            tweet = json.loads(tweet)
        except ValueError:
            pass
        if 'text' in tweet:
            text = tweet['text']
            words = text.split()
            words_set = set(words) # words is now a set
            pos = 0
            neg = 1
            for word in words_set:
                if word in sent_amounts:
                    if sent_amounts[word] > 0:
                        pos += 1
                    else:
                        neg += 1
            for word in words_set:
                if len(word) > 0:
                    if word not in sent_amounts:
                        term_sentiment[word].append(pos/float(neg))
    return compute_averages(term_sentiment)

def is_str(the_str):
    try:
        str(the_str)
        return True
    except:
        return False

def compute_averages(terms):
    for term, values_l in terms.iteritems():
        avg = sum(values_l) / float(len(values_l))
        try:
            print '{0} {1}'.format(term, avg)
        except UnicodeEncodeError:
            pass

def main():
    sent_amounts = create_sentiment(open(sys.argv[1]))
    tweet_file = open(sys.argv[2])
    output_term_sentiment(tweet_file, sent_amounts)


if __name__ == '__main__':
    main()
