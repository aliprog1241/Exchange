import requests
import json
import os

from config import url,rulse

#for API and response

def get_rates():  
    response = requests.get(url)
    if response.status_code == 200 :
        return json.loads(response.text)
    return None
    
#for run json code

def archive(filename, rates):
    if not os.path.exists("archive"):
        os.makedirs("archive")

    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates, indent=4))

#for email 

def send_mail(timestamp, rates):
    subject = f'{timestamp} rates'
    if rulse['preferred'] is not None :
        tmp = dict()
        for exc in rulse['preferred'] :
            tmp[exc] = rates[exc]
        rates = tmp


    text  = json.dumps(rates)


    


if __name__ == "__main__" :
    response = get_rates()
    if rulse['archive']:
        archive(response['timestamp'], response['rates'])
    if rulse['send_mail']:
        archive(response['timestamp'], response['rates'])
