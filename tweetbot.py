import RssFeeder
import tweepy

Feed = RssFeeder.Tweet_content

class TwitterAPI:
    def __init__(self):
        consumer_key = "1Q3LT2y48wZZ48IEm5sX0nx3z"
        consumer_secret = "5Doyp3ZHoX6Qfc3DpBDfqGY5kqEnrbZ586zkgfRSvIY15oWIuw"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "96121325-PGE0KPt6jipztQqr3izWEESCo5itpT5gjO27jJ9B2"
        access_token_secret = "Qj0S0EcQIaUgG09rXnaCMOM1DOjXMEKzhmIFIERlFf6Q0"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet(Feed)
