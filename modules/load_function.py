import os
import logging
import boto3

logger = logging.getLogger(__name__)

def load_to_s3(data_dir: str,AWS_ACCESS_KEY:str, AWS_SECRET_KEY:str,AWS_BUCKET:str):
    """function to extract json files from a url and save to a destination

    Args:
        data_dir (str): link data directory where the data files are to upload
        AWS_ACCESS_KEY (str): secret value from .env file
        AWS_SECRET_KEY (str): secret value from .env file
        AWS_BUCKET (str): secret value from .env file
    """

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
            return True
        except Exception as e:
            print(f'something went wrong 🫪, error {e}')
            logger.error(f'something went wrong, error {e}')
    return False