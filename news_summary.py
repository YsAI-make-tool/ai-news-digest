import feedparser
import google.generativeai as genai
import os

# Gemini APIキー設定
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

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

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)

    return response.text

if __name__ == "__main__":
    news = fetch_news()
    summary = summarize(news)
    print(summary)

