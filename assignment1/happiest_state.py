import sys
import json

from collections import defaultdict


def sort_dict_by_value(mappings, reverse=False):
    """
    Sorted in ascending order
    type mappings:   dict
    param mappings:  dict you want to sort

    returns a list of tuples with key, values [('key':1), ('key2':3), ...]
    """
    tuples = []
    for key, value in sorted(mappings.iteritems(), key=lambda (k,v): (v,k),
        reverse=reverse):
        tuples.append((key, value))
    return tuples


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

def obtain_sentiment_score(tweet, sent_amounts):
    sum = 0
    if 'text' in tweet:
        text = tweet['text']
        for t in text.split():
            if t in sent_amounts:
                sum += float(sent_amounts[t])
    return sum

def find_happiest_state(tweet_file, sent_amounts):
    states = defaultdict(float)
    for tweet in tweet_file:
        try:
            tweet = json.loads(tweet)
        except ValueError:
            pass
        if 'place' in tweet:
            place = tweet['place']

            if place is not None and 'country_code' in place\
                                                and 'full_name' in place:
                CC = place['country_code']
                names = place['full_name'].split(',')
                if len(names) == 2:
                    state_name = names[-1].strip()
                if CC == 'US':
                    states[state_name] += obtain_sentiment_score(tweet,
                            sent_amounts)
    happy_states = sort_dict_by_value(states, reverse=True)
    if len(happy_states) > 0:
        print(happy_states[0][0])


def main():
    sent_amounts = create_sentiment(open(sys.argv[1]))
    tweet_file = open(sys.argv[2])
    find_happiest_state(tweet_file, sent_amounts)


if __name__ == '__main__':
    main()

