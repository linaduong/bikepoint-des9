import os
import json
import time
from datetime import datetime
import requests

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
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
        except Exception as e:
            print(f'yikes! 😬 error occured when saving the json: {e}')
        break

    elif 300< status_code <500:
        print(f'api call failed 🤡, status code {status_code} 😔')
        break

    else:
        if attempts==max_attempts:
            print(f'max attempts reached, #skillissue? 🫪, status code: {status_code}')
        else:
            print(f'attempt {attempts}/{max_attempts} failed, status code {status_code}, will retry 🫡')
        attempt+=1
        time.sleep(30)

#print(data)
