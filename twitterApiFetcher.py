import requests
import os
import json
import time
from datetime import datetime, timedelta

my_secret = os.environ['token']
supabase_token = os.environ['supabase']
supabase_url = "https://qegerxvnmsvqhoxidyzq.supabase.co/rest/v1/tweets"

headers = {
    'apikey': supabase_token,
    'Authorization': 'Bearer '+supabase_token,
    'Content-Type': 'application/json',
    'Prefer': 'return=representation'
}

# current utc date as iso string
def get_date():
    return (datetime.utcnow() - timedelta(days=1)).isoformat()[0:19]+'z'

def api_fetcher(url):
    payload={}
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAPXBSgEAAAAAg4SpEcJmn5OG9VH7GxUMFCzCfKY%3DgorMtstrVvr4nw1SuEGBPWqmGaDhZ37GViHj5pLQjRLXNMFCBO',
        'Cookie': 'guest_id=v1%3A162897756963895564; personalization_id="v1_k/6FhTnjpoRl6DxUGZ7FZQ=="'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    return response.json()

def find_author_data(all_authors, author_id):
    for author in all_authors:
        if author['id'] == author_id:
            return author
            break

def find_attachment_data(all_attachments, attachment_id):
    for attachment in all_attachments:
        if attachment['media_key'] == attachment_id:
            return attachment
            break


def worker():
    iso_date = get_date()
    url = "https://api.twitter.com/2/tweets/search/recent?start_time="+iso_date+"&tweet.fields=id,text,created_at,entities&expansions=attachments.media_keys,author_id&media.fields=duration_ms,height,media_key,non_public_metrics,organic_metrics,preview_image_url,promoted_metrics,public_metrics,type,url,width&user.fields=id,name,username,profile_image_url,url&query=%23trabajoAr%20-is%3Aretweet"
    twitter_data = api_fetcher(url)
    for tweet in twitter_data['data']:
        tweet_id=tweet['id']
        tweet_text=tweet['text']
        tweet_author_id = tweet['author_id']
        tweet_created_date = tweet['created_at']
        tweet_entities = tweet['entities']
        if 'attachments' in tweet and 'media_keys' in tweet['attachments']:
            tweet_attachments = find_attachment_data(twitter_data['includes']['media'],tweet['attachments']['media_keys'][0])
        else:
            tweet_attachments = ''
        tweet_author = find_author_data(twitter_data['includes']['users'], tweet_author_id)
        
        payload = json.dumps({
          'id': tweet_id,
          'author_id': tweet_author_id,
          'author': tweet_author,
          'text': tweet_text,
          'created_date': tweet_created_date,
          'entities': tweet_entities,
          'attachments' : tweet_attachments
        })

        r = requests.request("POST", supabase_url, headers=headers, data=payload)
        print(r.text)
    print("FINISHED EXECUTION")


while True:
  worker()
  time.sleep(1000)