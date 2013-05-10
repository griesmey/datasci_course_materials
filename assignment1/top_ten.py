import json
import sys
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


def find_top_ten(tweet_file):
    tags = defaultdict(float)
    for tweet in tweet_file:
        try:
            tweet = json.loads(tweet)
        except ValueError:
            pass
        if 'entities' in tweet and 'hashtags' in tweet['entities']:
            hash_tags = tweet['entities']['hashtags']
            for tag in hash_tags:
                if 'text' in tag:
                    tags[tag['text']] += 1

    sorted_tags = sort_dict_by_value(tags, reverse=True)
    if len(sorted_tags) >= 10:
        top_ten = sorted_tags[:10]
    for i in top_ten:
        print '{0} {1}'.format(i[0], i[1])

def main():
    tweet_file = open(sys.argv[1])
    find_top_ten(tweet_file)

if __name__ == "__main__":
    main()