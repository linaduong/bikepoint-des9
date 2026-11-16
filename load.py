import os
import json
import logging
from dotenv import load_dotenv
import boto3

load_dotenv()

AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
AWS_BUCKET=os.getenv('AWS_BUCKET')

data_dir = 'data'
#make sure that it's a forward slash here!
file_location = os.listdir(data_dir)

s3_client = boto3.client(
    's3',
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_KEY
)

for file in file_location:
    to_upload = f'{data_dir}/{file}'
    try:
        #function, location name, name of the file to be uploaded
        s3_client.upload_file(to_upload, AWS_BUCKET, file)
        print(f'file {file} successfully uploaded! 🥳')
        os.remove(to_upload)
    except Exception as e:
        print(f'something went wrong 🫪, error {e}')