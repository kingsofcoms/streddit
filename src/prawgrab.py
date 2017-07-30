import datetime


import praw

c = '3EHSroJfEXyTPw'
s = 'jLfUQfaaV-nmbUZddGCvveBURFY'

reddit = praw.Reddit(client_id=c,
                     client_secret=s,
                     user_agent='praw')

today = datetime.date.today()

favorites = 'programming python cryptomarkets'

for favorite in favorites:
    for submission in reddit.subreddit(favorite).hot(limit=25):

        print "Reddit {} hot 25 on {}".format(
            favorite,
            datetime.now().strftime("%Y-%m-%d")
        )

        print "\n"

        print "1. [{}]({})".format(
            submission.title.encode('utf-8').strip(),
            submission.shortlink.encode('utf-8').strip()
        )
