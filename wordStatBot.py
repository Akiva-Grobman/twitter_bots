import operator
import re
import tweepy


class WordStatBot:

    def __init__(self, api, uid):
        self.api = api
        self.uid = uid
        # search limit
        self.LIMIT = 3199
        # dictionary of word and times of appearance (word, count)
        self._words_dict = dict()

    def print_top_tweets(self, tweets_to_print):
        tweet_count = 0
        for tweet in tweepy.Cursor(self.api.user_timeline, id=self.uid).items():
            tweet_count += 1
            # update word count
            self._update_dict(tweet_text=tweet.text)
            # stop if limit is passed
            if tweet_count >= self.LIMIT:
                break
        print(f'Checked {tweet_count} tweets')
        # sort by word count
        sorted_tweets = self._get_sorted()
        # not sure why but the tuples are in reversed order (this is a bandied and should be fixed)
        length = len(sorted_tweets) - 1
        # print top tweets_to_print tweets
        for i in range(tweets_to_print):
            print(f'#{i + 1} ({sorted_tweets[length - i][1]})\n\t{sorted_tweets[length - i][0]}')

    # updates the word dict (word, word count) dictionary with the text given as a param
    def _update_dict(self, tweet_text):
        tweet_text = cleanup_text(tweet_text)
        words = tweet_text.split()
        for word in words:
            if word in self._words_dict:
                self._words_dict[word] += 1
            else:
                self._words_dict[word] = 1

    # returns a list of tuples (word count, word) sorted by word count
    def _get_sorted(self):
        return sorted(self._words_dict.items(), key=operator.itemgetter(1))


# removes mentions and parenthesis
def cleanup_text(text):
    # remove mentions
    text = re.sub(r"(@)\w+\s", "", text)
    # remove parenthesis and punctuation symbols
    text = re.sub(r"[\([{})\]],.'\"", "", text)
    return text
