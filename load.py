import os
import json
import logging
from dotenv import load_dotenv
import boto3

load_dotenv()

AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
AWS_BUCKET=os.getenv('AWS_BUCKET')

test_file = '2026-11-11 15-30-37.json'
file_location = 'data/2026-11-11 15-30-37.json'

s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_KEY
)

s3_client.upload_file(file_location, AWS_BUCKET, test_file)