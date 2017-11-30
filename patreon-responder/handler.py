import os
import json
from validate import *
import hmac
import requests
import tweepy

def handle(st):
    req = json.loads(st)

    event_type = os.getenv("Http_X_Patreon_Event")
    sender_digest = os.getenv("Http_X_Patreon_Signature")

    key = os.getenv("webhook_secret")

    print("Event: " + event_type)

    if validate_hmac(sender_digest, key, st) == False:
        print("Bad HMAC from sender, could not verify")
        return

    if event_type == "pledges:create":
        cents = req["data"]["attributes"]["amount_cents"]

        patron_link = req["data"]["relationships"]["patron"]["links"]["related"]

        r = requests.get(patron_link)

        if r.status_code == 200:
            patron = r.json()
            twitter = patron["data"]["attributes"]["twitter"]
            tagged = ""
            if twitter != None and len(twitter) > 0:
                tagged = " @" + twitter
            tweet = patron["data"]["attributes"]["full_name"] + tagged + " just pledged " + "{0:.2f}".format(float(cents/100)) + " dollar(s) to @OpenFaaS. Thank you from #TeamServerless!"

            print(tweet)

            auth = tweepy.OAuthHandler(os.environ["consumer_key"], os.environ["consumer_secret"])
            auth.set_access_token(os.environ["access_token"], os.environ["access_token_secret"])

            api = tweepy.API(auth)

            try:
                print("Sending: " + tweet)

                api.update_status(tweet)
            except e:
                print(e)
