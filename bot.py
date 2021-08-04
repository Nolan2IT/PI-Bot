import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from eBayFetcher import eBayFetcher

fetcher = eBayFetcher()

bot = commands.Bot(command_prefix = '.')

load_dotenv() #load env variables
TOKEN = os.getenv('TOKEN') #gets token from .env file

@bot.event
async def on_ready():
    print("Bot Connected to the Server.")

@bot.command()
async def get(ctx, *, title):
    print(title)
    prodInfo = fetcher.fetch(title)
    response = f'**Title: {title.title()}** \n' 
    response += f'**NEW** - Average Price: {prodInfo["newCost"]} \t Number of Listings: {prodInfo["newCount"]} \n'
    response += f'**USED** - Average Price: {prodInfo["usedCost"]} \t Number of Listings {prodInfo["usedCount"]}'
    await ctx.send(response)

bot.run(TOKEN)