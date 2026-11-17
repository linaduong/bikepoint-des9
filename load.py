import os
import json
import logging
from datetime import datetime
from dotenv import load_dotenv
import boto3

load_dotenv()

timestamp = datetime.now().strftime('%Y-%m-%d')

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/load/{timestamp}.log'

#don't have to write on separate lines, but makes it easier to read
logging.basicConfig(
    filename = log_filename,
    #don't question the format - time - severity of the message - the actual message
    format = '%(asctime)s - %(levelname)s - %(message)s',
    #ignore anything that's below INFO
    level = logging.INFO
)

logger = logging.getLogger()
#logger.info can be found across all print statements, to log the outcome into the historic log
logger.info('logger was successfully initialised')

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
logger.info('connection to s3 successful')

for file in file_location:
    to_upload = f'{data_dir}/{file}'
    try:
        #function, location name, name of the file to be uploaded
        s3_client.upload_file(to_upload, AWS_BUCKET, file)
        print(f'file {file} successfully uploaded! 🥳')
        logger.info(f'file {to_upload} was successfully uploaded')
        os.remove(to_upload)
        logger.info(f'file {to_upload} was deleted locally')
    except Exception as e:
        print(f'something went wrong 🫪, error {e}')
        logger.error(f'something went wrong, error {e}')