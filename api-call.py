import os
import json
import time
import logging
from datetime import datetime
import requests

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
log_filename = f'{log_dir}/{timestamp}.log'

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

#print(timestamp)
data_dir = 'data'
#'exist_ok' is just so that the folder existing is okay
os.makedirs(data_dir, exist_ok=True)
filename = f'{data_dir}/{timestamp}.json'

url ='https://api.tfl.gov.uk/BikePoint/'

attempts = 1
max_attempts = 3

while attempts <= max_attempts:
    response = requests.get(url)
    status_code = response.status_code

    if 200<= status_code <300:
        try:
            #validating that data is in a json format
            data = response.json()
            #open is basically used to interact with the filename variable, with -w to mean write
            with open(filename, 'w') as file:
                #^aliasing the function to write in the file, as 'file'
                json.dump(data, file)
            print(f'great success!🥳🙌 file has been saved as "{filename}"')
            logger.info(f'file has been saved as "{filename}"')
        except Exception as e:
            print(f'yikes! 😬 error occured when saving the json: {e}')
            logger.error(f'error occured when saving the json: {e}')
        break

    elif 300< status_code <500:
        print(f'api call failed 🤡, status code {status_code} 😔')
        logger.error(f'api call failed, status code {status_code}')
        break

    else:
        if attempts==max_attempts:
            print(f'max attempts reached, #skillissue? 🫪, status code: {status_code}')
            logger.warning(f'max attempts reached, status code: {status_code}')
        else:
            print(f'attempt {attempts}/{max_attempts} failed, status code {status_code}, will retry 🫡')
            logger.error(f'attempt {attempts}/{max_attempts} failed, status code {status_code}, will retry')
        attempt+=1
        time.sleep(30)

#print(data)
