import tweepy
import json


def init_api():
    try:
        with open('keys.json', 'r') as key_json:
            config = json.load(key_json)
        auth = tweepy.OAuthHandler(config["CONSUMER_KEY"], config["CONSUMER_SECRET"])
        auth.set_access_token(config["ACCESS_KEY"], config["ACCESS_SECRET"])
        t_api = tweepy.API(auth,
                           wait_on_rate_limit=True,
                           wait_on_rate_limit_notify=True)
        t_api.verify_credentials()
        print("Verified")
        return t_api
    except json.JSONDecodeError:
        print("Problems with config.json")
        return None
