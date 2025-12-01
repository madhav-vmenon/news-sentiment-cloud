import pandas as pd
from textblob import TextBlob

def compute_sentiment(input_file="cleaned_articles.csv", output_file="articles_sentiment.csv"):
    # Read the CSV produced by transform()
    df = pd.read_csv(input_file)

    def get_sentiment(text):
        # Handle NaN / non-string
        if not isinstance(text, str):
            text = str(text or "")
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            label = "positive"
        elif polarity < 0:
            label = "negative"
        else:
            label = "neutral"
        # Return both in a Series so it becomes two new columns
        return pd.Series([polarity, label])

    # Apply sentiment analysis to the "cleaned_text" column
    df[["sentiment_polarity", "sentiment_label"]] = df["cleaned_text"].apply(get_sentiment)

    # Save CSV with sentiment included
    df.to_csv(output_file, index=False)
    print(f"Saved sentiment-enhanced data to {output_file}")
    return df

if __name__ == "__main__":
    compute_sentiment()

# import pandas as pd
# from textblob import TextBlob
#
#
# # def compute_sentiment(text):
# #     analysis = TextBlob(text)
# #     polarity = analysis.polarity
# #     label = 'positive' if polarity > 0 else 'negative' if polarity < 0 else 'neutral'
# #     return {"polarity": polarity, "label": label}
#
# def compute_sentiment(input_file="cleaned_articles.csv", output_file="articles_sentiment.csv"):
#     df = pd.read_csv(input_file)
#
#
#     def get_sentiment(text):
#         blob = TextBlob(text)
#         polarity = blob.sentiment.polarity
#         if polarity > 0:
#             label = "positive"
#         elif polarity < 0:
#             label = "negative"
#         else:
#             label = "neutral"
#
#         return pd.Series([polarity, label])
#
#     # Apply sentiment analysis to cleaned text
#     df[["sentiment_polarity", "sentiment_label"]] = df["cleaned_text"].apply(get_sentiment)
#
#     # Save CSV with sentiment included
#     df.to_csv(output_file, index=False)
#     print(f"Saved sentiment-enhanced data to {output_file}")
#     return df
#
# if __name__ == "__main__":
#     compute_sentiment()
#
#
#
#
