import requests
import json
username = 'bcsClass'
password = 'jaribuKuingia@bcs$$+++!XZty'
payload = {
    'username':username,
    'password':password
}
response = requests.post('https://isms.iaa.ac.tz/ismsapi/hakiki.php', verify=False, json = payload)
url_2 = 'https://isms.iaa.ac.tz/ismsapi/students.php'
auth_token = response.json().get('token')

headers = {
    'Authorization': f'Bearer {auth_token}',
    'Content-Type': 'application/json'
}
payload = {
    'username':'BCS_0073_2020',
    'password':'Ayaro2050'
}

ren = requests.post(url_2, headers=headers, verify=False, json = payload)
content = ren.json()
print(content)