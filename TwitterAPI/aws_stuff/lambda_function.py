import json
import random
import boto3
from requests_oauthlib import OAuth1Session

s3 = boto3.client('s3')
bucket = 'bushbot'

def postTweet(consumer_token, consumer_key, access_token, access_token_secret, msg):
    oauth = OAuth1Session(
        consumer_token,
        client_secret=consumer_key,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )
    payload = {"text": msg}

    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))
    # Saving the response as JSON
    return response.json()

def chooseTweet():
    key = 'quotes.json'
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']
    quotes = json.loads(content.read())

    num = quotes['totalCount']
    quotenum = random.randrange(0,num)
    msg = '"'
    msg += quotes['Quotes'][quotenum] + '"\n' + quotes['Date'][quotenum] + ',' + quotes['Location'][quotenum]
    return msg

def lambda_handler(event, context):
    key = 'secrets.json'
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body']

    secrets = json.loads(content.read())
    ct = secrets['consumer_token']
    ck = secrets['consumer_key']
    at = secrets['access_token']
    ats = secrets['access_key']
    print("Secrets", secrets)

    msg = chooseTweet()

    twitter_response = postTweet(ct, ck, at, ats, msg)
    return {
        'statusCode': 200,
        'body': json.dumps(twitter_response)
    }
