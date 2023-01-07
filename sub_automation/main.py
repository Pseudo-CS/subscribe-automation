import requests, os

def token():
    # note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
    auth = requests.auth.HTTPBasicAuth('VpHbyZzC-mQrJtdL95zlow', 'uXgDh2jvaq3DK0waW1LIAndIgJ_NuQ')

    # here we pass our login method (password), username, and password
    data = {'grant_type': 'password',
            'username': 'sazkikai',
            'password': '7353377510'}

    

    # send our request for an OAuth token
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers)

    # convert response to JSON and pull access_token value
    TOKEN = res.json()['access_token']
    print(TOKEN)


# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

TOKEN = '240176963445-ei9nlTKmrm6lXh4tZWdaWfGgOXSiMA'
# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}



f = open('sub.txt', 'r')
for i in f:
    # while the token is valid (~2 hours) we just add headers=headers to our requests
    res = requests.post('https://oauth.reddit.com/api/subscribe', headers=headers, data={'action':'sub', 'sr_name':i} )
    print(res.json)