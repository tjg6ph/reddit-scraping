#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import secret 
reddit = praw.Reddit(client_id=secret.client_id, \
                     client_secret=secret.client_secret, \
                     user_agent=secret.user_agent, \
                     username=secret.username, \
                     password=secret.password)
                     
subreddit = reddit.subreddit('Vaporwave')

topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in subreddit.top(limit=1):
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
        
comments_body = ['']
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    comments_body.append(comment.body)

topics_data = pd.DataFrame(topics_dict)
comments_data = pd.DataFrame(comments_body)
def get_date(created):
    return dt.datetime.fromtimestamp(created)
_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp = _timestamp)
topics_data.to_csv('vaporscrape_v1.csv', index=False)
comments_data.to_csv('vaporcomments_v1.csv', index=False)