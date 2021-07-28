import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

bot = commands.Bot(command_prefix = '.')

load_dotenv() #load env variables
TOKEN = os.getenv('TOKEN') #gets token from .env file
        
@bot.event
async def on_ready():
    print("Bot Connected to the Server.")

@bot.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

@bot.command()
async def kick(ctx, member : discord.Member, reason = None):
    await member.kick(reason = reason)

@bot.command()
async def ban(ctx, member : discord.Member, reason = None):
    await member.ban(reason = reason)

bot.run(TOKEN)