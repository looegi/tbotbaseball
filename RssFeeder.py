import feedparser

d = feedparser.parse('http://fivethirtyeight.com/economics/feed/')

Tweet_content = d.entries[0]['title'] + " " + d.entries[0]['link']
