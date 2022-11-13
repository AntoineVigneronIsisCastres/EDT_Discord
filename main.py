import asyncio
import datetime
from dotenv import load_dotenv
from discord.ext import tasks
import discord
import os
import edt_discord
from discord_webhook import DiscordWebhook, DiscordEmbed

client = discord.Client(intents=discord.Intents.default())
urlWebhook = "https://discord.com/api/webhooks/957043914735509624/HQyBkGpyTfBNYwNMSkKnfze5jlvaRzd2sznFD3szdJh4H1sP55AEWduvdjmqlczPmOmm"
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


def seconds_until(hours, minutes):
    given_time = datetime.time(hours, minutes)
    now = datetime.datetime.now()
    future_exec = datetime.datetime.combine(now, given_time)
    if (future_exec - now).days < 0:  # If we are past the execution, it will take place tomorrow
        future_exec = datetime.datetime.combine(now + datetime.timedelta(days=1), given_time) # days always >= 0

    return (future_exec - now).total_seconds()
    

@tasks.loop(hours=24)
async def daily_edt():
    while True:
        await asyncio.sleep(seconds_until(6,0))
        edt_discord.run_daily()
        await asyncio.sleep(60)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    print("aaaaaaaaaa")
    print(message.content)
    try:
        promo = message.content.split(' ')[1]
    except:
        promo = "fia4"
    print("bbbbbbbbbbbbbbbb")
        
    semaine = "False"
    jour = "False"
    try:
        if message.content.split(' ')[2] == 'semainepro':
            semaine = message.content.split(' ')[2]
        elif "/" in message.content.split(' ')[2]:
            semaine = message.content.split(' ')[2]
        elif message.content.split(' ')[2] in jours:
            jour = message.content.split(' ')[2]
    except:
        semaine = "False"
    print("ccccccccccccccccc")
    if message.content.startswith("!edt"):
        print("ddddddddddddddddddd")
        if semaine != "False":
            print("eeeeeeeeeeeeeeeeeeeeeeeee")
            edt_discord.run_semaine(promo, semaine)
        elif jour != "False":
            edt_discord.run_jour(promo, jour)


client.run(TOKEN)
