import tweepy
import configparser
from textblob import TextBlob
import time
from streamlistener import Listener

# keywords = ['Kanban', '#kanban', 'Scrum', '#scrum']
# keywords = ['Kanban', '#kanban']
keywords = ['Scrum', '#scrum']
languages = ['en', 'de']

config = configparser.ConfigParser()
config.read('config')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)
bot_id = int(api.verify_credentials().id)

try:
    # print(api.verify_credentials())
    print(f'Login successful (id: {bot_id})')
except tweepy.TweepyException as e:
    print(e)
except Exception as e:
    print(e)

stream_listener = Listener(api_key, api_key_secret, access_token, access_token_secret)

stream_listener.filter(track=keywords, languages=languages)
