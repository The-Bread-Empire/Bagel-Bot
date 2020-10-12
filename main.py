import discord
import os
import random
import time
from time import sleep
from keep_alive import keep_alive
from discord.ext import commands
import discord.utils
from discord.utils import get
from discord.ext.commands import Bot
import asyncio
from datetime import datetime
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from clear import clear

bot = commands.Bot(command_prefix="^", case_insensitive=True)


@bot.event
async def on_ready():
    clear()
    print("I'm in")
    print(bot.user)

#start of commands

@bot.command(name="blank")
async def on_message(ctx):
  await ctx.send("test")


@bot.command(name="dm")
async def id_(ctx, user: discord.User):
  await user.send("Good Birthday")



#end of commands
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
