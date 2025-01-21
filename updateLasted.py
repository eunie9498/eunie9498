import feedparser
uri = "https://kong-droid.com/rss"
feed = feedparser.parse(uri)

markdown_text = """
#### Latest Posting Check Here
"""

for i in feed['entries'][:5]:
	markdown_text += f"[{i['title']}]({i['link']}) <br>"

f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
