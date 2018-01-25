import praw
import re
import os
import pdb

# Create the reddit instance
reddit = praw.Reddit("bot")

if not os.path.isfile("replied.txt"):
    replied = []
else:
    with open("replied.txt", "r") as file:
        replied = file.read()
        replied = replied.split("\n")
        replied = list(filter(None, replied))

subreddit = reddit.subreddit("pythonforengineers")

for submission in subreddit.hot(limit=10):
    if submission.id not in replied:
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("Botty bot says: Me too!!")
            print "bot replying"
            replied.append(submission.id)
with open("replied.txt", "w") as file:
    for postID in replied:
        file.write(postID+"\n")
