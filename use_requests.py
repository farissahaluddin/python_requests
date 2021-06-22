import requests


url = 'https://kompas.com'
try:
    response = requests.get(url)
    if response.status_code==200:
        print(f'Success! {response.status_code}')
        print(f'Success! {response.text}')
    else:
        print(f'Salah request bossskuh {response.status_code}')
except Exception as lah:
    print(f'Error bos {lah}')
    print('End')