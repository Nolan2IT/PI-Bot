import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
from eBayFetcher import eBayFetcher
from googleapiclient.discovery import build

fetcher = eBayFetcher()

bot = commands.Bot(command_prefix = '.')

load_dotenv() #load env variables
TOKEN = os.getenv('TOKEN') #gets token from .env file
GOOGLE_TOKEN = os.getenv('GOOGLE_TOKEN') #gets token from .env file

@bot.event
async def on_ready():
    print("Bot Connected to the Server.")

@bot.command()
async def get(ctx, *, title):
    print(title)
    prodInfo = fetcher.fetch(title)
    response = f'**Title: {title.title()}**\n'
    if prodInfo["newCount"] != 0:
        response += f'**NEW** - Average Price: ${prodInfo["newCost"]} \t Number of Listings: {prodInfo["newCount"]} \t eBay Net Resell: ${float(prodInfo["newCost"])*.871-15:.2f}\n'
    else:
        response += f'**NEW** - No Results Found.'
    if prodInfo["usedCount"] != 0:
        response += f'**USED** - Average Price: ${prodInfo["usedCost"]} \t Number of Listings {prodInfo["usedCount"]} \t eBay Net Resell: ${float(prodInfo["usedCost"])*.871-15:.2f}'
    else:
        response += f'**USED** - No Results Found.'
    await ctx.send(response)

@bot.command()
async def show(ctx, *, title):
    print(title)
    prodInfo = fetcher.fetch(title)
    response = f'**Title: {title.title()}**\n'
    if prodInfo["newCount"] != 0:
        response += f'**NEW** - Average Price: ${prodInfo["newCost"]} \t Number of Listings: {prodInfo["newCount"]} \t eBay Net Resell: ${float(prodInfo["newCost"])*.871-15:.2f}\n'
    else:
        response += f'**NEW** - No Results Found.'
    if prodInfo["usedCount"] != 0:
        response += f'**USED** - Average Price: ${prodInfo["usedCost"]} \t Number of Listings {prodInfo["usedCount"]} \t eBay Net Resell: ${float(prodInfo["usedCost"])*.871-15:.2f}'
    else:
        response += f'**USED** - No Results Found.'
    #Use Google's API to get image of product
    resource = build("customsearch", "v1", developerKey = GOOGLE_TOKEN).cse()
    result = resource.list(
        q = f"{title}", cx = os.getenv('cx'), searchType = 'image'
    ).execute()
    url = result['items'][0]['link']
    embed1 = discord.Embed(description = response)
    embed1.set_thumbnail(url = url)
    #embed1.set_image(url = url)
    await ctx.send(embed = embed1)

bot.run(TOKEN)