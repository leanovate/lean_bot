import pandas as pd
import tweepy
import os


#
# class Listener(tweepy.Stream):
#     def __init__(self, api):
#         self.api = api
#         self.me = api.verify_credentials()
#
#     def on_status(self, tweet):
#         if tweet.in_reply_to_status_id is not None or tweet.use.id == self.me.id:
#             return
#
#         if not tweet.retweeted:
#             try:
#                 # tweet.retweet()
#                 print(f"{tweet.author.screen_name} - {tweet.text}")
#                 print(f"Tweet ({tweet.in_reply_to_status_id}) retweeted successfully")
#             except Exception as e:
#                 print(e)
#
#         if not tweet.favorited:
#             try:
#                 # tweet.favorite()
#                 print(f"Tweet ({tweet.in_reply_to_status_id}) favorited successfully")
#             except Exception as e:
#                 print(e)
#
#     def on_error(self, status):
#         print(f"Error while retweeting: {status}")


class Listener(tweepy.Stream):
    # def __init__(self, api):
    #     self.api = api
    #     self.me = api.verify_credentials()

    tweets = []
    limit = 10
    file_path = './export_tweets.csv'

    def on_status(self, tweet):
        self.tweets.append(tweet)
        if not tweet.truncated:
            print(f'\n{tweet.user.screen_name}: {tweet.text}')

        else:
            print(f'\n{tweet.user.screen_name}: {tweet.extended_tweet["full_text"]}')

        if len(self.tweets) == self.limit:
            self.handle_export(self.tweets)
            self.disconnect()

    def on_error(self, status):
        print(f"Error while retweeting: {status}")

    def handle_export(self, tweets):
        columns = ['User', 'Tweet']
        data = []
        for tweet in self.tweets:
            if not tweet.truncated:
                data.append([tweet.user.screen_name, tweet.text])
            else:
                data.append([tweet.user.screen_name, tweet.extended_tweet['full_text']])

        df = pd.DataFrame(data, columns=columns)
        if os.path.exists(self.file_path) and os.stat(self.file_path).st_size > 0:
            print('\nTweets exported.')
            df.to_csv(self.file_path, mode='a', header=False)
        else:
            print('\nNew export file created.')
            df.to_csv(r'./export_tweets.csv', index=False)
