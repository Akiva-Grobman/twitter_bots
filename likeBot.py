import tweepy


class LikeBot:

    def __init__(self, api, limit=200):
        self.api = api
        self.LIMIT = min(limit, 200)

    def like_tweets_excluding_replies(self, uid, print_count=False):
        self._like_tweet(False, uid, print_count)

    def like_tweets_including_replies(self, uid, print_count=False):
        self._like_tweet(True, uid, print_count)

    def _like_tweet(self, include_replies, uid, print_count):
        count = 0
        for tweet in tweepy.Cursor(self.api.user_timeline, id=uid).items():
            if (include_replies or tweet.in_reply_to_status_id is None) and not tweet.favorited:
                if count >= self.LIMIT:
                    break
                count += 1
                if print_count:
                    print(f'#{count}')
                tweet.favorite()




