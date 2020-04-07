#! usr/bin/env python3
import pandas as pd
import requests
import json
import csv

# http://api.pushshift.io/reddit/search/submission/?subreddit=vaporwave&before=1356998400&size=500 #

def getPushshiftData(after, before, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?size=1000&after='+str(after)+'&before='+str(before)+'&subreddit='+str(sub)
    r = requests.get(url)
    data = json.loads(r.text)
    return data['data']

#list of post ID's
post_ids = []
#Subreddit to query
sub='vaporwave'
# Unix timestamp of date to crawl from.
# 2018/04/01
after = '1575158400'
before = '1575763199'

data = getPushshiftData(after, before, sub)

# Will run until all posts have been gathered 
# from the 'after' date up until todays date
while len(data) > 0:
    for submission in data:
        post_ids.append(submission["id"])
    # Calls getPushshiftData() with the created date of the last submission
    data = getPushshiftData(sub=sub, after=data[-1]['created_utc'], before=data[-1]['created_utc'])

obj = {}
obj['sub'] = sub
obj['id'] = post_ids
# Save to json for later use
with open("submissions.json", "w") as jsonFile:
    json.dump(obj, jsonFile)