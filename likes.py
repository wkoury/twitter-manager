import tweepy
import secrets
import time

auth = tweepy.OAuthHandler(secrets.api_key, secrets.api_key_secret)
auth.set_access_token(secrets.access_token, secrets.access_token_secret)

api = tweepy.API(auth)

favorites = api.favorites()

while len(favorites) > 0:
    print("Found ", len(favorites), " tweets.")

    for tweet in favorites:
        print(favorites.index(tweet), "/", len(favorites), ": ")
        print(tweet.text)
        print()
        api.destroy_favorite(tweet.id)
        time.sleep(2)
    
    favorites = api.favorites()

print("No more new tweets to unlike!")
