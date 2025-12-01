from fetch_article import fetch_articles
from article_summarizer import transform
from sentiment import compute_sentiment
from upload_s3 import upload_to_s3

def run_all():
    print("1) Fetching news...")
    fetch_articles()  # use defaults or pass query, page_size here

    print("2) Transforming to cleaned CSV...")
    transform()

    print("3) Computing and adding sentiment...")
    compute_sentiment()

    print("4) Uploading to S3...")
    upload_to_s3("raw_news.json", "raw/raw_news.json")
    upload_to_s3("cleaned_articles.csv", "processed/cleaned_articles.csv")
    upload_to_s3("articles_sentiment.csv", "processed/articles_sentiment.csv")


    print("Pipeline complete. Check articles_sentiment.csv")

if __name__ == "__main__":
    run_all()