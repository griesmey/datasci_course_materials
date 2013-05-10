import sys
import json
from collections import defaultdict
import re


def compute_term_frequency(tweet_file):

    term_counts = defaultdict(int)
    count = 0
    for tweet in tweet_file:
        try:
            tweet = json.loads(tweet)
        except ValueError:
            pass
        if 'text' in tweet:
            text = tweet['text']
            words = text.split()
            for word in words:
                if len(word) > 0:
                    term_counts[word] += 1
                    count += 1
    return output_frequncy(term_counts, count)

def output_frequncy(counts, all_count):
    for i, value in counts.iteritems():
        try:
            print '{0} {1}'.format(i, value/float(all_count))
        except UnicodeEncodeError as e:
            pass

def main(tweet_filename):
    compute_term_frequency(open(tweet_filename))

if __name__ == '__main__':
    main(sys.argv[1])
