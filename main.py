from dotenv import load_dotenv
import discord
import os
import edt_discord

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    try:
        promo = message.content.split(' ')[1]
    except:
        promo = "fia4"
        
    try:
        if message.content.split(' ')[2] == 'semainepro':
            semaine = message.content.split(' ')[2]
        elif "/" in message.content.split(' ')[2]:
            semaine = message.content.split(' ')[2]
    except:
        semaine = "False"
    
    if message.content.startswith("!edt"):
        edt_discord.run(promo, semaine)

client.run(TOKEN)
