import os
import json
import time
import logging
import requests

logger = logging.getLogger(__name__)

def extract_to_json(url:str, data_dir: str, timestamp: str, max_attempts: int, delay:int):
    #3 speech marks, then crtl + shft + 2
    """function to extract json files from a url and save to a destination

    Args:
        url (str): put in url for the api
        data_dir (str): link data directory for data to save to
        timestamp (str): timestamp to append to file
        max_attempts (int): set maximum times that the script will retry
        delay (int): set the value in seconds how long to wait between each call
    """
    
    #make directory if it doesn't exist
    os.makedirs(data_dir, exist_ok=True)

    #build out the file name
    filename = f'{data_dir}/{timestamp}.json'

    attempts = 1

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

                #flag that data was saved successfully
                return True
            
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
            attempts+=1
            time.sleep(delay)

    #return statement - what it spits out at the end of the code after it runs
    return False
