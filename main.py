import logging
import os
from datetime import datetime
from dotenv import load_dotenv
from modules.extract_function import extract_to_json
from modules.load_function import load_to_s3

load_dotenv()

AWS_ACCESS_KEY=os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY=os.getenv('AWS_SECRET_KEY')
AWS_BUCKET=os.getenv('AWS_BUCKET')

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'

#don't have to write on separate lines, but makes it easier to read
logging.basicConfig(
    filename = log_filename,
    #don't question the format - time - severity of the message - the actual message
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    #ignore anything that's below INFO
    level = logging.INFO
)

logger = logging.getLogger()
#logger.info can be found across all print statements, to log the outcome into the historic log
logger.info('logger was successfully initialised')

url ='https://api.tfl.gov.uk/BikePoint/'
data_dir = 'data'

extract_to_json(url, data_dir, timestamp, max_attempts=3, delay=10)

print(extract_to_json)

load_to_s3(data_dir,AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_BUCKET)

print(load_to_s3)