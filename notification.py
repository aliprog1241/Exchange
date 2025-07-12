import json
from kavenegar import *
# from local_config import KAVENEGAR_API_KEY
from config import rules


KAVENEGAR_API_KEY = ('637651586E4E705075374930626A7A56726653586D6D48465A66476B7370654F7351326B786474614473593D')


def send_notification(msg):
    try:
        api = KavenegarAPI(KAVENEGAR_API_KEY)
        params = {
            'sender': '2000660110',  # optional
            'receptor': rules['notification']['receiver'],
            'message': msg,
        }
        response = api.sms_send(params)
        print("SMS sent:", response)
    except APIException as e:
        print("API error:", e)
    except HTTPException as e:
        print("HTTP error:", e)


'''کد های بدرد نخور جهت یاد آوری اشتباهات'''

# try:
#     api = KavenegarAPI(KAVENEGAR_API_KEY)
#     params = {
#         'sender': '2000660110',#optional
#         'receptor': '09199983035',#multiple mobile number, split by comma
#         'message': "rules['preferred']",
#     } 
#     response = api.sms_send(params)
#     print(response)
# except APIException as e: 
#     print(e)
# except HTTPException as e: 
#     print(e)



# params = { 'sender' : '2000660110', 'receptor': '09199983035', 'message' :'yasin'}
# response = api.sms_send(params)


# def send_sms(txt):
#     try:
#         api = KavenegarAPI(KAVENEGAR_API_KEY)
#         params = {
#             'sender': '2000660110',
#             'receptor':rulse['notification']['receiver'],
#             'message': txt 
#         }   
#         response = api.sms_send(params)
#         print(str(response))
#     except APIException as e: 
#             print (str(e))
#     except HTTPException as e: 
#             print (str(e))