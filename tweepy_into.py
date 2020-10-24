import tweepy


consumer_key = "EbLsNEhcdBkRsQEscDwB12h7o"
consumer_secret = "tmXkeZLLtdySkgxgW7kXE06MAi3FBSJXiydQfczJ3UBATIBcym"
access_token = "2878924280-BUF2MIuMum4yqX6M640nrxTQze1cxC469INeT0M"
access_token_secret = "9LH7YvH7WdVMdqDXVxW7Wud6Yy0m6zfMXeSo7wutlbTKh"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
	print("**************************************")
	print(tweet.text)