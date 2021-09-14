import requests
import os
import json
import time

def worker():
  my_secret = os.environ['API_KEY']
  supabase_url = "https://qegerxvnmsvqhoxidyzq.supabase.co/rest/v1/tweets"

  response = requests.get("https://trabajoar-d6c63-default-rtdb.firebaseio.com/.json")

  data = response.json();
  try:
    for date in data:
      for tweet in data[date]:
        raw_tweet_data = data[date][tweet]
        firebase_id = tweet
        tweet_id = raw_tweet_data["id"]
        author_id = raw_tweet_data["author_id"]
        author = raw_tweet_data["author"]
        text = raw_tweet_data["text"]
        created_date = raw_tweet_data["created_at"]
        entities = raw_tweet_data["entities"]

        payload = json.dumps({
          'id': tweet_id,
          'author_id': author_id,
          'author': author,
          'text': text,
          'created_date': created_date,
          'entities': entities
        })

        headers = {
          'apikey': my_secret,
          'Authorization': 'Bearer '+my_secret,
          'Content-Type': 'application/json',
          'Prefer': 'return=representation'
        }

        r = requests.request("POST", supabase_url, headers=headers, data=payload)
        print(r.text)

  except:
    print("An exception occurred")
  
  new_headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }

  new_response = requests.request("DELETE", "https://trabajoar-d6c63-default-rtdb.firebaseio.com/.json", headers=new_headers)

  print(new_response.text)

while True:
  worker()
  time.sleep(1000)