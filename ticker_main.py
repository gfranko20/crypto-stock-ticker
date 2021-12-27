import requests
import pandas as pd
from bs4 import BeautifulSoup 
import time
from datetime import datetime
from market_open import current_day, is_time_between, market_open

#Get current time, used for testing purposes
def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

#create a crypto class 
class crypto:
    #object takes coin_type argument so pass ticker symbol in as str
    def __init__(self, coin_type):
        self.coin_type = coin_type

    #pull the data from yahoo finance and extract price    
    def pull_data(self):
        page  = requests.get("https://finance.yahoo.com/cryptocurrencies/")
        soup = BeautifulSoup(page.content, 'html.parser')
        coin_string = self.coin_type+"-USD"
        data_string = {"data-symbol": coin_string}
        crypto = soup.find(attrs=data_string).text
        return crypto
    #print the price and current time to the terminal
    def print_price(self):
        price = self.pull_data()
        print("The price of "+self.coin_type+" is: $" + price)
       


while True:
    
    BTC = crypto("BTC")
    ADA = crypto("ADA")
    MATIC = crypto("MATIC")

    BTC.print_price()
    ADA.print_price()
    MATIC.print_price()

    time.sleep(25)

 