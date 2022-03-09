
import diceroll
import discord
from discord.ext import commands
import asyncio

dice = ''
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('\n!!!= = = 256 Status: On = = =!!!\n')


@client.event
async def on_message(message):
    channel = message.channel
    msg = message.content

    if 'd' in message.content and message.content[0].isdecimal:
        dice = diceroll.roll(msg)

        await channel.send(dice)    
        
        

from tokenbot import token256
client.run(token256())
