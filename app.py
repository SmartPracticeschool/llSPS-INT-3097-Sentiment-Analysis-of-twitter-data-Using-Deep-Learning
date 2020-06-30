from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = '9oQD0Wz6JsBFYWLeAleqi3eJk'
consumer_secret = 'rdbLeDk1Ro1EAFb6t5P87whgSFIg9rjgOFJDyH4NgjHRxgkbI6'

access_token = '1276146197376401414-onWmQvJxVG8rFd5yiaknEu4YiTIuOX'
access_token_secret = 'MppEMUuShsDLIC9oTY2Pz7vpnPUNdH6Vznpvp1sHRrr2P'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})

app.run(debug=True)