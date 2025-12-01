import boto3
from botocore.exceptions import ClientError
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET_NAME

def upload_to_s3(file_path, key, bucket_name=S3_BUCKET_NAME):
    s3 = boto3.client(
        "s3",
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_KEY,
        region_name = AWS_REGION
    )
    try:
        s3.upload_file(file_path, bucket_name, key)
        print(f"Uploaded to S3: s3://{bucket_name}/{key}")
    except ClientError as e:
        print(f"Failed to upload {file_path} to {bucket_name}/{key}")
        print("Reason:", e)

    # try:
    #     s3.upload_file(file_path, bucket_name, key)
    #     print("Uploaded to S3:", key)
    # except ClientError as e:
    #     print("Failed to upload")



if __name__ == "__main__":
    upload_to_s3("articles_sentiment.csv", "my_bucket_name", "articles_sentiment.csv")