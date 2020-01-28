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
top_list = subreddit.top(limit=500)
test_list = list(top_list)
test_list[0].comments.list()[0].body