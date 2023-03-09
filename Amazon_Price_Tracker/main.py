from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
import os

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')
BUY_PRICE=1600


headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66",
    "Accept-Language":"en-US,en;q=0.9"
}


url="https://www.amazon.in/Airdopes-141-Bluetooth-Wireless-Playtime/dp/B09N3ZLB3T/ref=sr_1_6?crid=3S1H5VPJLWFVZ&keywords=airpod&qid=1659576621&sprefix=airpo%2Caps%2C431&sr=8-6"
response=requests.get(url,headers=headers)
web_html=response.text
soup=BeautifulSoup(web_html,"html.parser")
data=soup.find(name="span",class_="a-price-whole")
price=(data.get_text())
if "," in price:
    t,h=price.strip(".").split(",",2)
    price=float(t)+float(h)
else:
    price = float(price)
print(price)
p_title=soup.find(name="span",id="productTitle")
title=p_title.get_text().strip()

# Set up the email parameters
if price < BUY_PRICE:
    def send_email(subject, body, sender=email, recipients='t8831780@gmail.com', password=password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        smtp_server.quit()

    subject = "Amazon Price Alert!!"
    body = f"{title} is now at {price}"
    sender = "t8831780@gmail.com"
    recipients = email
    Password = password

    send_email(subject, body, sender, recipients, Password)
