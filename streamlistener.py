import tweepy

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
    def on_status(self, tweet):

        if not tweet.truncated:
            print(f'{tweet.user.screen_name}: {tweet.text}')
        else:
            print(f'{tweet.user.screen_name}: {tweet.extended_tweet["full_text"]}')

        # if len(self.tweets) == self.limit:
        #     self.disconnect()

    def on_error(self, status):
        print(f"Error while retweeting: {status}")
