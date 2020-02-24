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

submission = reddit.submission(url='https://www.reddit.com/r/Vaporwave/comments/ezcapb/i_made_a_vaporwave_inspired_remix_of_astral/')
submission.comments.replace_more(limit=None)
comments_data = []

for comment in submission.comments.list():
    comments_data.append(comment.body)

comments_data = pd.DataFrame(comments_data)
comments_data.to_csv('vaporcomments_v1.csv', index=False)