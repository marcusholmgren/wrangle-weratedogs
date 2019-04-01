import tweepy


def get_api():
    consumer_key = 'YOUR CONSUMER KEY'
    consumer_secret = 'YOUR CONSUMER SECRET'
    access_token = 'YOUR ACCESS TOKEN'
    access_secret = 'YOUR ACCESS SECRET'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

