#blizzard test

import praw
import pandas as pd
import datetime as dt
from textblob import TextBlob

reddit = praw.Reddit(client_id='0STBJJrrTH53SA', 
                     client_secret='7ttL7PpTdf6CrjfFiJJz4xJdQlg', 
                     user_agent='Social_Media_Mining_Project', 
                     username='NicCage4life', 
                     password='Texasfans131')


submission = reddit.submission(url="https://www.reddit.com/r/aww/comments/dvbb7b/my_grandpa_96_and_my_grandma_94_celebrating_their/")

submission = reddit.submission(id="dvbb7b")

sublist = []
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    sublist.append(comment.body)

with open('happytest.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(sublist))

new_list= []

for w in sublist:
	testimonial= TextBlob(w)
	testimonial.sentiment
	new_list.append(testimonial.sentiment.polarity) #-1 bad , #1 good 
	print(sum(new_list)/len(new_list)) #average






 

  
