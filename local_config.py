from kavenegar import *
api = KAVENEGAR_API_KEY = ('637651586E4E705075374930626A7A56726653586D6D48465A66476B7370654F7351326B786474614473593D')
params = { 'sender' : '2000660110', 'receptor': '09199983035', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
response = api.sms_send(params)