#Imports
import disnake
from disnake.ext import commands
import json


#JSON load
with open("config.json", "r") as f:
    config = json.load(f)

#General
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=config["prefix"], intents=intents)
bot.remove_command("help")


#on_ready event
@bot.event
async def on_ready():
    print("Online.")


#Cog list
extensions = [
    'cogs.Main',
    'cogs.Admin',
    'cogs.Activity',
    'cogs.Fun'
]

#Cycle for to load a extensions
for extension in extensions:
    bot.load_extension(extension)

#Run
bot.run(config["token"])
