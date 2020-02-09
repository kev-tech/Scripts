import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.newegg.com/p/pl?d=western+digital+easystore").text
soup = BeautifulSoup(page, "html.parser")

title = soup.findAll("a", {"class": "item-title"})
price = soup.findAll("li", {"class": "price-current"})
shipping = soup.findAll("li", {"class": "price-ship"})


# Outputs First Product
title_print = print(title[0].text.strip())
price_print = print(price[0].text.strip())
shipping_print = print(shipping[0].text.strip())


# Outputs All Products
for r in title:
    print(r.text.strip())

for r in price:
    print(r.text.strip())
    
for r in shipping:
    print(r.text.strip())
