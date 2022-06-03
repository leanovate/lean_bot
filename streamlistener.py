import tweepy
import pandas as pd
import os


class Listener(tweepy.Stream):

    tweets = []
    limit = 100
    file_path = './tweets.csv'

    def on_status(self, tweet):

        if hasattr(tweet, "retweeted_status"):
            return

        # TODO check if tweet is own tweet

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
            df.to_csv(r'./tweets.csv', index=False)
