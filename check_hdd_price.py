from urllib.request import urlopen
import re
import subprocess
import time
import smtplib, ssl
from bs4 import BeautifulSoup

port = 465
sender = 'pythonicemails@gmail.com' #Change string to your desired send-from address.
password = input("Enter your gmail password: ")
recipient = 'mail@kevtech.co'
message = ''

url = 'https://www.newegg.com/p/2WA-0006-004A7?Description=western%20digital%20easy%20store&cm_re=western_digital_easy_store-_-9SIA8X5AJ26384-_-Product' #URL to crawl.
page = urlopen(url).read()
soup = BeautifulSoup(page, features="html.parser")
result = ''
price = ''

def check_price():
    price = soup.find('div', attrs={'div':'aside'})
    message = 'price is: {}'.format(price)
    print(message) #To delete.

def send_email():
    check_price()
    # context = ssl.create_default_context()
    # with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #     server.login(sender, password) #Change email address to send from here.
    #     server.sendmail(sender, recipient, message)

send_email()

#TODO: 
# - Incorrectly searching for aside/price-current HTML class.
# - Add other urls to crawl. 
# - Format email. 
