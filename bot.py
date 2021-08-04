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
    response = f'Average Cost: {prodInfo["avgCost"]}, Number of Listings: {prodInfo["count"]}'
    await ctx.send(response)

bot.run(TOKEN)