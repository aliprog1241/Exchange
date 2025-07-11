BASE_PATH = 'https://data.fixer.io/api/latest?access_key='

API_KEY = 'b4e56a512b6cc81723b2135671694f3f'

url = BASE_PATH + API_KEY 

EMAIL_RECEIVER = 'miri03369@gmail.com'



"""rulse = {
    'archive': True,
    'send_mail': True,
    'preferred' : ['BTC', 'IRR', "USD", "CAD" ]
}
"""
rulse  = {
    'archive' : True,
    'email':{
        'send_mail' : True,
        'preferred' : ['BTC', 'IRR', "USD", "CAD" ],
    },
    'notification':{
        'enable' : True,
        'receiver' : '09199983035',
        'preferred' :{
            'BTC' : {'min':9.852039e-06, 'max':9.932039e-06},
            'IRR':{'min':49231.957393 , 'max':49244.957393},

        }

        
    }

}