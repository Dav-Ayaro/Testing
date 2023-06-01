import requests

url = 'https://isms.iaa.ac.tz/ismsapi/hakiki.php'
username = 'bcsClass'
password = 'jaribukuingia@bcs$$+++!XZty'

data = {
    'username': username,
    'password': password
}

try:
    response = requests.post(url, data=data, verify=False)
    response.raise_for_status()  # Raise an exception if the request was not successful
    token = response.text

    # Use the token for subsequent API requests
    print('Authentication Token:', token)
except requests.exceptions.RequestException as e:
    print('Error:', e)
