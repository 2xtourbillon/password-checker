import requests

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/rangssae/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetchin: {res.status_code}, check the api and try again.')

def pwned_api_check(password):
    #check password if it exists in API response
    pass