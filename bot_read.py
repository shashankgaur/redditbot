import praw

reddit = praw.Reddit('trialbot')

subreddit = reddit.subreddit("movies")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("URL: ", submission.url)
    print("Score: ", submission.score)
    print("---------------------------------\n")
