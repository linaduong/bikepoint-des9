import logging
import os
from datetime import datetime
from dotenv import load_dotenv
from modules.extract_function import extract_to_json
from modules.load_function import load_to_s3
from modules.logging_function import logging_setup

load_dotenv()

AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
AWS_BUCKET=os.getenv('AWS_BUCKET')

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

logging_setup('logs',timestamp)

url ='https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'

extract_to_json(url, data_dir, timestamp, max_attempts=3, delay=10)

if extract_to_json:
    load_to_s3(data_dir,AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_BUCKET)

else:
    logging.error(f'error in extracting data from bikepoint api, no data and therefore aborted')