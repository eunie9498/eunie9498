import feedparser
uri = "https://kong-droid.com/rss"
feed = feedparser.parse(uri)

velog_feed = feedparser.parse("https://velog.io/rss/@kong-droid")

markdown_text = """


<a href="mailto:bvegemilb@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-c5221f?style=flat-square&logo=Gmail&logoColor=white"/></a>



## ⚒️ 기술스택

Kotlin, Coroutine, Hilt, MVVM, MPAndroidChart, RoomDB, REST API, DataBinding, ViewBinding, Dagger2, CustomLayout, RxJava, Java




## ⚙️ Tools

Android Studio, Figma, Zeplin, GitHub, Git, Swagger, Amplitude, Atom, Slack, Jira, Confluence, Notion,




![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=eunie9498&show_icons=true&theme=radical)



## ✅  Latest Posting Check Here 

"""

for i in feed['entries'][:5]:
	markdown_text += f"[{i['title']}]({i['link']}) <br>"

for i in velog_feed['entries'][:5]:
	markdown_text += f"[{i['title']}]({i['link']}) <br>"



f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
