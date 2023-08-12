#imports
from disnake.ext import commands
import disnake
import sys


#class create
class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #cog listener to print status in terminal
    @commands.Cog.listener()
    async def on_ready(self):
      print('admin cog - ACTIVATED\n')

#setup cog file
def setup(bot):
    bot.add_cog(admin(bot))
