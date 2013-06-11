import sys
import json

"""
Get the sentiment from tweets of data file
"""

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

def generate_tweets_sent(tweet_file, sent_amounts):

    for tweet in tweet_file:
        sum = 0
        try:
            tweet = json.loads(tweet)
        except ValueError:
            pass
        if 'text' in tweet:
            text = tweet['text']
            for t in text.split():
                if t in sent_amounts:
                    sum += float(sent_amounts[t])
            print sum

def main():
    sent_amounts = create_sentiment(open(sys.argv[1]))
    tweet_file = open(sys.argv[2])
    generate_tweets_sent(tweet_file, sent_amounts)


if __name__ == '__main__':
    main()
