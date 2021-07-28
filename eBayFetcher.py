import os
import datetime
from dotenv import load_dotenv
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

load_dotenv() #load env variables
TOKEN = os.getenv('EBAY_TOKEN')

class eBayFetcher(object):
    def __init__(self, TOKEN):
        self.token = TOKEN

    def fetch(self):
        try:
            api = Connection(appid = self.token, config_file = None)
            response = api.execute('findItemsAdvanced', {'keywords': 'legos'})

            assert(response.reply.ack == 'Success')
            assert(type(response.reply.timestamp) == datetime.datetime)
            assert(type(response.reply.searchResult.item) == list)

            item = response.reply.searchResult.item[0]
            assert(type(item.listingInfo.endTime) == datetime.datetime)
            assert(type(response.dict()) == dict)

        except ConnectionError as e:
            print(e)
            print(e.response.dict())
    
    def parse(self):
        pass

if __name__ == '__main__':
    e = eBayFetcher(TOKEN)
    e.fetch()
    e.parse()