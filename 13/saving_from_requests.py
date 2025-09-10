import requests

response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()

with open('romeo_and_juliet.txt', 'wb') as play_file:
    for chunk in response.iter_content(100_000):
        play_file.write(chunk)
