import tweepy
import json


api_key = "pqQSGDYC9TlXYxT6mgjb3si4F"
api_secret = "YspqL96gk3AEKcE5230TrbYahz28RHdtVW3UrTwMlV2QAcKvEK"
access_token_key = "18301790-nvMfMrm0PYvDYfnaYHSehYEfZtZDkC2IaJ7OQrPZI"
access_token_secret = "P3b3K5LMfSWH1QiwgNrD0ewtAlgeFOb2wrGCO83OVIzvl"

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

# for tweet in tweepy.Cursor(api.search,
#                            q="twitter",
#                            rpp=100,
#                            result_type="recent",
#                            include_entities=True,
#                            lang="en",
#                            geocode="17.3660,78.4760,5000km"
#                            ).items():
# #     print tweet
#     print tweet.created_at, tweet.text.encode("utf-8")
    
print api.trends_daily(date='2014-11-25')
