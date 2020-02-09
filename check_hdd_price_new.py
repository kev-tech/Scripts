import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.newegg.com/p/pl?d=western+digital+easystore").text
soup = BeautifulSoup(page, "html.parser")

title = soup.findAll("a", {"class": "item-title"})
price = soup.findAll("li", {"class": "price-current"})
shipping = soup.findAll("li", {"class": "price-ship"})

filename ="poducts.txt"

f = open(filename, "w")



# prints the first product on the page.
title_print = print(title[0].text.strip())
price_print = print(price[0].text.strip())
shipping_print = print(shipping[0].text.strip())


# prints all the products on the page.
for r in title:
    print(r.text.strip())

for r in price:
    print(r.text.strip())
    
for r in shipping:
    print(r.text.strip())

f.write([title_print])
f.write(price_print)
f.write(shipping_print)
f.close()