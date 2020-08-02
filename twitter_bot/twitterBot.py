import tweepy


CONSUMER_KEY = 'add your consumer key'
CONSUMER_SECRET = 'add your consumesecretr '
ACCESS_TOKEN='add your token '
ACCESS_TOKEN_SECRET='add your acces token secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# api.update_status("Bot Test 001")
queries = ["100daysofcode", "hackclub"]
tweets_per_query = 50
new_tweets = 0
for query in queries:
    print("Starting new query" + query)
    for tweet in tweepy.Cursor(api.search, q = query, tweet_mode="extended").items(tweets_per_query):
        user = tweet.user.screen_name
        id = tweet.id
        url = 'https://twitter.com/' + user + '/status/' + str(id)
        print(url)

        try:
            text = tweet.retweeted_status.full_text.lower()
        except:
            text = tweet.full_text.lower

        if "100daysofcode" in text or "hackclub" in text:
            if not tweet.retweeted:
                try:
                    tweet.retweet()
                    print("\tRetweeted")
                    new_tweets += 1
                except tweepy.TweepError as e:
                    print('\tAlredy Retweeted')
        if"like" in text or "fav" in text:
            try:
                tweet.favorite()
                print('\t'+"Liked")
            except:
                print('\t Already Liked')

print("New Tweets: " + str(new_tweets))




