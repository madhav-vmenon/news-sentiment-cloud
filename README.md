News-Sentiment to Cloud Insights Pipeline

This project builds an end-to-end analytics pipeline that:
- Fetches recent news articles from NewsAPI
- Downloads full article texts from the web
- Cleans and summarizes each article
- Performs sentiment analysis (polarity + positive/neutral/negative)
- Uploads the final dataset to AWS S3

It showcases skills in:
- Python (data processing, NLP)
- APIs (NewsAPI)
- Cloud (AWS S3, boto3)
- Basic NLP (TextBlob, Newspaper3k)

## Project Structure

```text
project/
├── data_fetch/
│   └── fetch_article.py
├── cleaning/
│   ├── clean_text.py
├── summarizing/
│   ├── article_summarizer.py
├── analytics/
│   └── sentiment.py
├── cloud/
│   └── upload_s3.py
├── utils/
│   └── config.py
├── raw_news.json       # created after fetching articles
├── cleaned_articles.csv
├── articles_sentiment.csv
├── requirements.txt
└── README.md