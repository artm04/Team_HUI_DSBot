#imports
from disnake.ext import commands
import disnake


#json load
with open('config.json', 'r') as f:
  config = json.load(f)


#general
intents = disnake.Intents.all()
bot = disnake.Bot(commands_prefix=config['prefix'], intents=intents)
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
for extension in extension:
  bot.load_extension(extension)

#run
bot.run(config['token'])
