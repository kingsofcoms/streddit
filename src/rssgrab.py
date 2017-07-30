from datetime import datetime


import feedparser


favorites = 'programming python cryptomarkets golf jokes'.split()

def url(sub):
    return "http://www.reddit.com/r/{}/.rss".format(sub)

for favorite in favorites:

    print "\n =============================="
    print "Reddit {} hot 25 on {}\n".format(
        favorite,
        datetime.now().strftime("%Y-%m-%d")
    )

    feed = feedparser.parse(url(favorite))

    for entry in feed.entries:

        print "1. [{}]({})".format(
            entry.title.encode('utf-8').strip(),
            entry.link.encode('utf-8').strip()
        )
