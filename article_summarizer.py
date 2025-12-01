import json
import pandas as pd
from newspaper import Article
from clean_text import clean_article

def transform(input_file="raw_news.json", output_file="cleaned_articles.csv"):
    with open(input_file) as f:
        raw = json.load(f)

    articles = raw["articles"]
    rows = []

    for a in articles:
        url = a["url"]

        # Try to fetch + parse full article body
        try:
            article_obj = Article(url)
            article_obj.download()
            article_obj.parse()
            article_obj.nlp()
        except Exception as e:
            # If anything goes wrong (403, parsing failure, etc),
            # log it and skip this article instead of crashing.
            print(f"[SKIP] Failed to process URL: {url}")
            print(f"       Reason: {e}")
            continue

        title = article_obj.title
        authors = ", ".join(article_obj.authors) if article_obj.authors else ""
        publish_date = article_obj.publish_date
        full_text = article_obj.text
        summary = getattr(article_obj, "summary", "")

        cleaned_text = clean_article(full_text)

        rows.append({
            "title": title,
            "authors": authors,
            "published": publish_date,
            "url": url,
            "full_text": full_text,
            "cleaned_text": cleaned_text,
            "summary": summary,
            "publishedAt": a.get("publishedAt"),
            "source": a.get("source", {}).get("name"),
        })

    # If every article failed, avoid crashing on empty list
    if not rows:
        print("No articles were successfully processed. Check logs above.")
        return None

    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)
    print(f"Saved cleaned article data to {output_file} with {len(df)} rows")
    return df

if __name__ == "__main__":
    transform()

# import json
# import pandas as pd
# from newspaper import Article
# from clean_text import clean_article
# from sentiment import compute_sentiment
#
# def transform(input_file="raw_news.json", output_file="cleaned_articles.csv"):
#     with open(input_file) as f:
#         raw = json.load(f)
#
#     # Extract the list of articles from the JSON under the "articles" key
#     articles = raw["articles"]
#     # Create an empty list to store processed article data
#     rows = []
#
#     for a in articles:
#         url = a["url"]
#
#         article_obj = Article(url)
#         article_obj.download()  # fetches HTML content
#         article_obj.parse()
#         article_obj.nlp()
#
#         # Store the article metadata
#         title = article_obj.title
#         authors = ", ".join(article_obj.authors) if article_obj.authors else ""
#         publish_date = article_obj.publish_date
#
#         # Use full article text for cleaning + sentiment
#         full_text = article_obj.text
#         cleaned_text = clean_article(full_text)
#         sentiment = compute_sentiment(cleaned_text)  # returns polarity + label
#         summary = article_obj.summary
#
#         rows.append({
#             "title": title,
#             "authors": authors,
#             "published": publish_date,
#             "url": url,
#             "cleaned text": cleaned_text,
#             "sentiment": sentiment,
#             "publishedAt": a["publishedAt"],  # publication date from API
#             "source": a["source"]["name"]  # source name from API
#         })
#
#         df = pd.DataFrame(rows)
#         df.to_csv("cleaned_sentiment.csv", index=False)
#
#         return df
#
#
# # Run transform if this file is executed directly
# if __name__ == "__main__":
#     transform()
#




'''
import tkinter as tk
import nltk
from textblob import TextBlob


def summarize():
    url = utext.get('1.0', "end").strip()

    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', "end")
    title.insert('1.0', article.title)

    author.delete('1.0', "end")
    author.insert('1.0', article.authors)

    publication.delete('1.0', "end")
    publication.insert('1.0', str(article.publish_date))

    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0',f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')



root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publication Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()



root.mainloop()
'''


