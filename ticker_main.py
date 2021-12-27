import requests
from bs4 import BeautifulSoup 
import time

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

#Creates a class for Stonks
class stonk:
    #object takes stock_type argument so pass ticker symbol in as str
    def __init__(self, stock_type):
        self.stock_type = stock_type
    #pull the data from yahoo finance and extract price    
    def pull_data(self):
        #As long as url follows same pattern (which it did in testing) this should work for any stock
        url = "https://finance.yahoo.com/quote/"+self.stock_type+"?p="+self.stock_type+"&.tsrc=fin-srch"
        page  = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        stock = soup.find(attrs={"data-symbol": self.stock_type}).text
        return stock
    #print the price to the terminal
    def print_price(self):
        price = self.pull_data()
        print("The price of "+self.stock_type+" is $"+price)

#Infinite loop that instantiates stonk/crypto objects and then applies the print_price method
while True:
    F = stonk("F")
    AAPL = stonk("AAPL")

    F.print_price()
    AAPL.print_price()

    BTC = crypto("BTC")
    ADA = crypto("ADA")
    MATIC = crypto("MATIC")

    BTC.print_price()
    ADA.print_price()
    MATIC.print_price()


    #Sleep for 25 seconds
    time.sleep(25)

 
