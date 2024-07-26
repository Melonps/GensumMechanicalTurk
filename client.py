import os

import boto3
from dotenv import load_dotenv


def get_client():
    load_dotenv()
    # MTurkクライアントの作成
    client = boto3.client(
        "mturk",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name="us-east-1",
        endpoint_url="https://mturk-requester-sandbox.us-east-1.amazonaws.com",
    )
    return client
