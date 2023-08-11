#imports
from disnake.ext import commands
import disnake
import json


#json load
with open('config.json', 'r') as f:
  config = json.load(f)


#general
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)
bot.remove_command('help')

#on_ready event
@bot.event
async def on_ready():
  print('Team bot is ACTIVATED\n')

#cog list
extensions = [
  'cogs.main'
]

#cycle for to install cog files
for extension in extensions:
  bot.load_extension(extension)

#run
bot.run(config['token'])
