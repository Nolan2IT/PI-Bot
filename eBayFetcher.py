import os
import datetime
from dotenv import load_dotenv
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

load_dotenv() #load env variables
TOKEN = os.getenv('EBAY_TOKEN')

class eBayFetcher(object):
    def __init__(self):
        self.api = Connection(appid = TOKEN, config_file = None)

    def fetch(self, title = None): # , productCondition = None
        try:
            response = self.api.execute('findItemsAdvanced', {'keywords': title})
            #print(response.reply)
            avgCost = 0.0
            count = 0
            for item in response.reply.searchResult.item:
                print(f"Title: {item.title}, Price {item.sellingStatus.currentPrice.value}")
                #if "New" == productCondition:
                avgCost += float(item.sellingStatus.currentPrice.value)
                count += 1
            avgCost /= count
            prodInfo = {'avgCost' : f"{avgCost:.2f}", 'count' : count}
            print(prodInfo)
            return prodInfo    


        except ConnectionError as e:
            print(e)
            print(e.response.dict())
    
    def parse(self):
        pass

if __name__ == '__main__':
    e = eBayFetcher(TOKEN)
    e.fetch()