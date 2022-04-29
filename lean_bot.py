import tweepy
import configparser
from textblob import TextBlob
import time

config = configparser.ConfigParser()
config.read('config')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
bot_id = int(api.me().id_str)

mention_id = id
while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        print(f'Mention: {mention.text} - {mention.author.screen_name}')
        mention_id = mention.id
        mention_analysis = TextBlob(mention.text)
        mention_analysis_score = mention_analysis.sentiment.polarity
        print(f'Tweet has polarity score of {mention_analysis_score}')
        if mention.in_reply_to_status_id is None and mention.author.id != bot_id:
            if mention_analysis_score >= 0.3 and not mention.retweeted:
                try:
                    print('trying to retweet...')
                except Exception as err:
                    print(err)
            else:
                print('Tweet will not be retweeted')
    time.sleep(30)
