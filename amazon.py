# Import libraries
import requests
from bs4 import BeautifulSoup
import smtplib
import re
import time
import datetime
import csv
import pandas as pd 
import os

# Get your url from the amazon website and assign in the url variable
url = 'https://www.amazon.ae/Samsung-Galaxy-Ultra-Mobile-Smartphone/dp/B084GQCNJH/ref=sr_1_9?crid=22F7MZH4NA1FR&keywords=samsung%2Bs20&qid=1698838851&sprefix=samsung%2Bs20%2Caps%2C1726&sr=8-9&th=1'

# Create your user agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
# Create check price function
def check_phone_price():
    # Ask the requests library to get the url data
    page = requests.get(url,headers=headers)
    
    # Use the bs4 library to read the data
    bs = BeautifulSoup(page.content, 'html.parser')
    
    # Show the user the data you are scraping from the amazon website
    #print(bs.prettify().encode("utf-8"))
    
    # How to get the specific data
    #Get the title  from the amazon website
    product_title = bs.find(id="productTitle").get_text().strip()
    
    # Show the user the data you are scraping from the amazon website
    print(product_title)
    
    #Get the price  from the amazon website
    product_price = bs.find("span", attrs={"class": 'a-price-whole'}).get_text()
    
    # Show the user the data you are scraping from the amazon website
    print(product_price)
    
    # Use regular expressions to remove non-numeric characters or bad symbols
    clean_price = re.sub(r'[^0-9]', '', product_price)
    print(clean_price)
    
    # Convert the text to float
    price_float = float(clean_price)
    
    
    # Create a report in csv  to your folder
    today = datetime.date.today()
    header = ['Title','Price', 'Date']
    data = [product_title,price_float,today]
    with open("AmazonScrapedDataset.csv", 'w', newline="", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerow(data)
        return check_phone_price
    # Open CSv file
    df = pd.read_csv(r"C:\Users\user\Desktop\AmazonKamtule\AmazonScrapedDataset.csv")
    print(df)
    
    print(price_float)
    return(price_float)
    
# Sending Email to your account when the prices are fluctuating
def send_email():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('kamtulethokozani1@gmail.com', "xxxxxxxxxxx")
    subject = "Hey! the price fell down. Do you want to buy?"
    body = "Go order now before the price fluctuates\n Link: https://www.amazon.ae/Samsung-Galaxy-Ultra-Mobile-Smartphone/dp/B084GQCNJH/ref=sr_1_9?crid=22F7MZH4NA1FR&keywords=samsung%2Bs20&qid=1698838851&sprefix=samsung%2Bs20%2Caps%2C1726&sr=8-9&th=1"
    msg = f"Subject : {subject}\n\n\n{body}"
    server.sendmail('kamtulethokozani1@gmail.com', "xxxxxxxxxxx",msg)
    #print("email sent")
    server.quit()
    
# Call functions
#price = check_phone_price()
# Write if statement
#if(price ==1400.0):
    send_email()