import requests
import json
import os

# KEY: WPahYarP85QoflEnEznxYoGgWWmBnVuDfD1ck7vB
# https://api.nasa.gov/planetary/apod?api_key=WPahYarP85QoflEnEznxYoGgWWmBnVuDfD1ck7vB
# Account ID: 891ec21f-4cfd-4361-a22c-515e3c77f471

KEY = os.environ.get('NASA_KEY')


count = 10

url = f"https://api.nasa.gov/planetary/apod?api_key={KEY}&count={count}"

r = requests.get(url)

print(r.status_code)


events_data = r.json()

with open('POTD.json', 'w') as f:
    f.write(json.dumps(events_data, indent=4))


with open("POTD.txt", 'w') as f:
    for i in range(count):
        f.write(events_data[i]['url'] + '\n')
        print(events_data[i]['url'])
