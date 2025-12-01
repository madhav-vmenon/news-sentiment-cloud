import os
from dotenv import load_dotenv

load_dotenv()

# Pulls your NewsAPI key from environment variables
# Inside .env you have: NEWS_API_KEY=your_key_here
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Your AWS access key used for authentication to AWS from code
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")

# The matching AWS secret key
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

AWS_REGION = "us-east-1"

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

