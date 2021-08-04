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
            #print(f"Title: {item.title}, Price {item.sellingStatus.currentPrice.value}, Condition: {item.condition.conditionDisplayName}, LT: {item.listingInfo.listingType}")
            newAvgCost = 0.0
            newCount = 0
            usedAvgCost = 0.0
            usedCount = 0
            newKeyWords = {'New', 'Digital Good', 'Like New', 'New-open box','Open box', 'New with tags', 'New without tags', 'New with defects', 'New with box', 'New without box', 'Brand New', 'New other (see details)'}
            usedKeyWords = {'Used', 'Very Good' 'Good', 'Acceptable', 'Certified refurbished', 'Seller refurbished', 'Pre-owned', 'Certified pre-owned', 'Remanufactured', 'Retread'}
            for item in response.reply.searchResult.item:
                try:
                    if(item.listingInfo.listingType == 'FixedPrice' or item.listingInfo.listingType == 'StoreInventory'):
                        #print(item.condition.conditionDisplayName)
                        if item.condition.conditionDisplayName in newKeyWords:
                            newAvgCost += float(item.sellingStatus.currentPrice.value)
                            newCount += 1
                        elif item.condition.conditionDisplayName in usedKeyWords:
                            usedAvgCost += float(item.sellingStatus.currentPrice.value)
                            usedCount += 1    
                except:
                   pass
                
            newAvgCost /= newCount
            usedAvgCost /= usedCount
            #for item
            prodInfo = {'newCost' : f"{newAvgCost:.2f}", 'newCount' : newCount, 'usedCost' : f"{usedAvgCost:.2f}", 'usedCount' : usedCount}
            print(prodInfo)
            return prodInfo    


        except ConnectionError as e:
            print(e)
            print(e.response.dict())
    
    def parse(self):
        pass

if __name__ == '__main__':
    e = eBayFetcher()
    e.fetch()
    e.parse()