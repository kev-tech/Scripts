#Uses python 2 for easier share with coworkers.
import urllib2
import re
import subprocess
import time

url = 'https://store.ui.com/products/unifi-dream-machine' #URL to crawl.
page = urllib2.urlopen(url).read()
result = ''

def stock_check():
  sold_out = re.findall('Sold Out', page)

  if len(sold_out) == 0:
    message = "The Product is in stock!"
  else:
    message = "Product is not available :()"

  result = subprocess.check_output(['echo', message])
  print(result)

while True: 
  stock_check()
  time.sleep(60)
