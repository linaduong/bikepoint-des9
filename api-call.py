import os
import json
from datetime import datetime
import requests

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#print(timestamp)
data_dir = 'data'
#'exist_ok' is just so that the folder existing is okay
os.makedirs(data_dir, exist_ok=True)
filename = f'{data_dir}/{timestamp}.json'

url ='https://api.tfl.gov.uk/BikePoint/'

response = requests.get(url)

#validating that data is in a json format
data = response.json()

#open is basically used to interact with the filename variable, with -w to mean write
with open(filename, 'w') as file:
    #aliasing the function to write in the file, as 'file'
    json.dump(data, file)

#print(data)