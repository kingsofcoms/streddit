# core
from datetime import datetime

# 3rd party
import pyperclip
import feedparser

# local modules
pass



class RSSFeed(object):

    @property
    def clipboard(self):
        txt = str(self)
        pyperclip.copy(txt)
        return txt

    @property
    def date(self):
        return datetime.now().strftime("%Y-%m-%d")

    @property
    def feed(self):
        s = ''
        for entry in self.rss_feed.entries:

            s += "1. [{}]({})\n".format(
                entry.title.encode('utf-8').strip(),
                entry.link.encode('utf-8').strip()
            )

        return s

    @property
    def rss_feed(self):
        feed = feedparser.parse(self.url)
        return feed

    def __str__(self):
        return "{}\n{}".format(self.title, self.feed)


class Reddit(RSSFeed):

    def __init__(self, sub):
        self.sub = sub

    @property
    def url(self):
        return "http://www.reddit.com/r/{}/.rss".format(self.sub)

    @property
    def title(self):
        return "Reddit {} hot 25 on {}\n".format(
            self.sub,
            self.date
        )




class HackerNews(RSSFeed):

    @property
    def title(self):
        return "Hacker News {}\n".format(
            self.date,
        )

    @property
    def url(self):
        return 'http://news.ycombinator.com/rss'

def main():

    favorite_subs = 'jokes python programming'.split()
    for sub in favorite_subs:
        reddit = Reddit(sub)
        print reddit.clipboard
        raw_input('Press enter to continue: ')

    hacker_news = HackerNews()
    print hacker_news.clipboard


if __name__ == '__main__':
    main()
