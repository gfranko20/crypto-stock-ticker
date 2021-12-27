# crypto-ticker



The goal of ths project is to create a ticker that displays current prices of different cryptos and stocks. In its current form, a crypto or stock object is instantiated with its ticker symbol pass in as a string. This symbol must be in all caps and match exactly as it appears on Yahoo Finance. This occurs within an infinite while loop. When the print_price method is called, the current price will be determined using the pull_data method. This uses beautiful soup to grab the html from Yahoo Finance and then creates a dictionary using the coin/stock type to locate the price in the html. The price will then be printed to the termial. The infinite while loop also currently includes as 25 second waiting period as it takes time for the data to update. Based on my testing it seems that prices update about every five minutes. Eventually, instead of printing to the terminal it will pass prices directly to the ticker hardware.
