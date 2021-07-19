from api import init_api
# from likeBot import LikeBot
# from wordStatBot import WordStatBot


def main():
    api = init_api()

    # word_stat = WordStatBot(api, '@AkivaGrobman')
    # word_stat.print_top_tweets(10)

    # like_bot = LikeBot(api)
    # like_bot.like_tweets_excluding_replies('@salomon_yossi', True)


if __name__ == '__main__':
    main()

