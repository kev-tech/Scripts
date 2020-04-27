#Uses python 2 for easier share with coworkers.
from urllib.request import urlopen
import re
import subprocess
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv
from twilio.rest import Client

stop = False

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

client = Client(account_sid, auth_token)

url = 'https://shop.aukey.com/products/omnia-61w-pd-charger'
page = urlopen(url).read().decode('utf-8')
result = ''



def check_availability():
  amazon = re.findall('Discount on Amazon', page)
  add_to_card = re.findall('Add to cart', page)

  if len(amazon) == 0 and len(add_to_card) == 0:
    message = "No dice, kev."
  else:
    message = "Buy it now!"
    message = client.messages.create(
    body='100w Charger is in stock!',
    from_='+17633332162',
    to='+18573450733'
    )
    
    stop = True
  
  result = subprocess.check_output(['echo', message])
  print(result)

while stop == False: 
  check_availability()
  time.sleep(60)
