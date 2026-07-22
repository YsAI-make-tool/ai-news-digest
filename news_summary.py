import feedparser
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

RSS_FEEDS = [
    "https://news.yahoo.co.jp/rss/topics/it.xml",
    "https://news.yahoo.co.jp/rss/topics/computer.xml",
    "https://news.yahoo.co.jp/rss/topics/science.xml"
]

def fetch_news():
    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:3]:
            articles.append(entry.title + " - " + entry.link)
    return "\n".join(articles)

def summarize(text):
    prompt = f"以下のニュースを3行で要約してください:\n{text}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    news = fetch_news()
    summary = summarize(news)
    print(summary)
