import requests

__author__ = "pkpacheco"

request = requests.get("https://www.google.com")

print(request.content)
