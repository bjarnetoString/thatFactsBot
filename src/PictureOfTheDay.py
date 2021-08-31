import requests
import json
import os


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
