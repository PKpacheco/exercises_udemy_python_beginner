# coding=UTF-8
import requests
from bs4 import BeautifulSoup

__author__ = "pkpacheco"

request = requests.get("http://www.johnlewis.com/john-\
                       lewis-henry-chair-leather-seat/p325451?colour=Black")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
print(element.text.strip())

# <span itemprop="price" class="now-price"> £199.00 </span>
