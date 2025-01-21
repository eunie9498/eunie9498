import feedparser
uri = "https://kong-droid.com/rss"
feed = feedparser.parse(uri)

markdown_text = """
![header](https://capsule-render.vercel.app/api?type=wave&color=auto&height=300&section=header&text=Hi, I'm Android Developer %20render&fontSize=90)


<a href="mailto:bvegemilb@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-c5221f?style=flat-square&logo=Vimeo&logoColor=white"/></a>



## ⚒️ 기술스택

Kotlin, Coroutine, Hilt, MVVM, MPAndroidChart, RoomDB, REST API, DataBinding, ViewBinding, Dagger2, CustomLayout, RxJava, Java




## ⚙️ Tools

Android Studio, Figma, Zeplin, GitHub, Git, Swagger, Amplitude, Atom, Slack, Jira, Confluence, Notion,




![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=eunie9498&show_icons=true&theme=radical)



## ✅  Latest Posting Check Here 

"""

for i in feed['entries'][:5]:
	markdown_text += f"[{i['title']}]({i['link']}) <br>"



f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
