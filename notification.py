#!/usr/bin/env python
import json
from kavenegar import *
import json

from local_config import KAVENEGAR_API_KEY

from config import rulse


def send_sms(txt):
    try:
        api = KavenegarAPI(KAVENEGAR_API_KEY)
        params = {
            'sender': '20006535',
            'receptor':rulse['notification']['receiver'],
            'message': txt 
        }   
        response = api.sms_send(params)
        print(str(response))
    except APIException as e: 
            print (str(e))
    except HTTPException as e: 
            print (str(e))