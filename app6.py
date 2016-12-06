# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

__author__ = "pkpacheco"

request = requests.get("http://www.johnlewis.com/john-\
                       lewis-henry-chair-leather-seat/p325451?colour=Black")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = (element.text.strip())

price_without_symbol = (string_price[1:])

price = float(price_without_symbol)

if price < 200:
    print ("You shold buy the chair!")
    print("The current price is {} ".format(price))
else:
    print ("Do not buy, it's too expensive")


# <span itemprop="price" class="now-price"> £199.00 </span>
