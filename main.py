from dotenv import load_dotenv
import discord
import os

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content == "!edt":
        __import__("edt_discord")

client.run(TOKEN)