import discord
#import edt_discord.py
import os

client = discord.Client()
TOKEN = 'OTYwODc4NzI2Mjk0NDI5NzI2.Ykw2DA.d8OCoCmN_ecliPc07cdq3obDlLQ'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
client.run(TOKEN)