# lean_bot
### A twitter bot that will retweet and like to certain subjects

### Requierements
- tweepy  
- configparser  
- textblob  

Requirements are listed in `requirements` file and can be easly installed (it is recommended to do this within a virtual environment)

```
$ python -m venv .env

$ source .env/bin/activate

$ pip install -r requirements
```

### Setup
Credentials are being stored in an extra file and loaded via `configparser`.  
Defined file format:
```
[twitter]

api_key = abcdefg
api_key_secret = gfedcba
access_token = 1234567890abcd
access_token_secret = cba0987654321

```
