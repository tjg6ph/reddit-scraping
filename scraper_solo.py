#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import secret 

def get_date(created):
    return dt.datetime.fromtimestamp(created)

def get_comment_text(comment_forest):
    # takes a list of comment forests
    # needs recursion
    master_list = []
    # HELLO TANNER -  THE ERROR IS SOMEWHERE IN HERE
    for comment in comment_forest.replies:
        master_list.append((comment.body,get_date(comment.created_utc)))
        if comment.replies:
            master_list.append(get_comment_text(comment))
    # END MESSAGE TO TANNER
    return master_list

reddit = praw.Reddit(client_id=secret.client_id, \
                     client_secret=secret.client_secret, \
                     user_agent=secret.user_agent, \
                     username=secret.username, \
                     password=secret.password)

# more complicated URL with multiple threaded comments - https://www.reddit.com/r/Vaporwave/comments/cus5f8/i_make_music_for_gifs_building_up_an_80s_track/?sort=confidence

submission = reddit.submission(url='https://www.reddit.com/r/Vaporwave/comments/ezcapb/i_made_a_vaporwave_inspired_remix_of_astral/')
submission.comments.replace_more(limit=None)
comments_data = []

comment_queue = submission.comments
traversed_comments = []
for comment in comment_queue:
    # add the comment regardless
    get_comment_text(comment)
    traversed_comments.append((comment.body,get_date(comment.created_utc)))
    if comment.replies:
        # if the comment also has replies, add all those
        for nested_comment in comment.replies:
            traversed_comments.append(get_comment_text(comment))
#            traversed_comments.append((nested_comment.body,get_date(comment.created_utc)))
    
traversed_comments = pd.DataFrame(traversed_comments)
traversed_comments.to_csv('vaporcomments_v1.csv', index=False)