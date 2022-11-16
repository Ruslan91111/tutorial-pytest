import requests

from configuration import SERVICE_URL

def getting_posts():
    response = requests.get(url=SERVICE_URL)
    print(response.json())



getting_posts()