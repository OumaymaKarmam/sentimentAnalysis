import snscrape.modules.twitter as sntwitter
import sys
from tools.tweet_listener import TweetStreamListener

def main():
    # Obtain the input topics of your interests
    topics = []
    if len(sys.argv) == 1:
        # Default topics
        topics = ['Congress']
    else:
        for topic in sys.argv[1:]:
            topics.append(topic)
    
    # Change this if you're not happy with the index and type names
    index = "tweet-sentiment"
    doc_type = "new-tweet"

    print("==> Topics", topics)
    print("==> Index: {}, doc type: {}".format(index, doc_type))
    print("==> Start retrieving tweets...")

    # Create instance of the tweepy tweet stream listener
    listener = TweetStreamListener(
                        index,
                        doc_type
                        )
    # Creating list to append tweet data to
    tweets_list1 = []

    for t in topics:
        # Using TwitterSearchScraper to scrape data and append tweets to list
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(t).get_items()):
            if i>100:
                break
            listener.on_data(tweet.content)



if __name__ == '__main__':
    main()
