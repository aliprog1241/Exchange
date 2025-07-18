


import requests
import json
import os

from config import url,rules
from notification import send_notification 

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
    if 'preferred' in rules['email'] and rules['email']['preferred']:
        tmp = dict()
        for exc in rules['email']['preferred']:
            if exc in rates:
                tmp[exc] = rates[exc]
        rates = tmp



    text  = json.dumps(rates)
    print(subject)
    print(text)
# add  notification


import jdatetime
import datetime

def check_notify_rules(rates):
    preferred = rules['notification']['preferred']
    msg = ''

    # Add current Jalali date
    now = datetime.datetime.now()
    jalali_date = jdatetime.datetime.fromgregorian(datetime=now).strftime('%Y/%m/%d %H:%M')
    msg += f'📅 تاریخ: {jalali_date}\n\n'

    for exc, limits in preferred.items():
        if exc in rates:
            rate = rates[exc]
            if rate <= limits['min']:
                msg += f'{exc} reached min {rate}\n'
            elif rate >= limits['max']:
                msg += f'{exc} reached max {rate}\n'
            else:
                msg += f'{exc} is OK: {rate}\n'

    return msg





if __name__ == "__main__":
    response = get_rates()
    if rules['archive']:
        archive(response['timestamp'], response['rates'])
    if rules['email']['send_mail']:
        send_mail(response['timestamp'], response['rates'])  # only if this function exists
    if rules['notification']['enable']:
        notification_msg = check_notify_rules(response['rates'])
        if notification_msg:
        
            send_notification(notification_msg)
