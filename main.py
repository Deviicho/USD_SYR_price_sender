import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import os


url = 'https://sp-today.com/en'
page = requests.get(url)


def main(page):
    src = page.content
    soup = BeautifulSoup(src , 'lxml')
    
    header = soup.find('header' , {'class' : 'navbar-fixed-top'})
    a = header.find('a' , {'href' : 'https://sp-today.com/en/currency/us_dollar/city/damascus'})
    USD_price = a.find('span' , {'class' : 'value'})
    SYRtoUSD =USD_price.text.strip()
    
    header = soup.find('header' , {'class' : 'navbar-fixed-top'})
    a = header.find('a' , {'href' : 'https://sp-today.com/en/gold/karat21'})
    GOLD_price = a.find('span' , {'class' : 'value'})
    GOLD_GRAM = GOLD_price.text.strip()
    
    sender = os.getenv('SENDER')
    app_password = os.getenv('APP_PASSWORD')
    receiver = ['michoar777@gmail.com', 'thomas.caroline7@gmail.com'] #use ', '

    msg = MIMEText(f"Good morning 👋🏽!\n\n\nhere is some news for today:\n\nthe price for 💲 is : {SYRtoUSD}\nand the price for 🪙 21k is : {GOLD_GRAM}")
    msg['Subject'] = 'Daily prices'
    msg['From'] = sender
    msg['To'] = 'Undisclosed Recipients <>'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg, to_addrs=receiver) 
    
    
main(page)



