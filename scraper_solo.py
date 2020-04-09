#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import secret 

def get_date(created):
    return dt.datetime.fromtimestamp(created)

reddit = praw.Reddit(client_id=secret.client_id, \
                     client_secret=secret.client_secret, \
                     user_agent=secret.user_agent, \
                     username=secret.username, \
                     password=secret.password)

import csv

def parse_urls_from_csv(csv_file='posts_master.csv'):
    """Given a csv, return the URLs contained in it"""


    base_url = 'http://reddit.com'
    urls = []

    with open(csv_file, encoding="utf8") as csv_in:
        csv_reader = csv.reader(csv_in, delimiter=',')
        for row in list(csv_reader)[1:]:
            urls.append(base_url + row[7])
    
    return urls

urls = parse_urls_from_csv()
comments = []
for url in urls:    
    submission = reddit.submission(url)
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        comments.append(comment.body)

comments = pd.DataFrame(comments)
comments.to_csv('vaporcomments_v1.csv', index=False)