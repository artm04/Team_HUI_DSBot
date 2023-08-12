#Imports
import disnake
from disnake.ext import commands
import json


#JSON load
with open("path/to/file", "r") as f:
  author = json.load(f)

#Author var.
author = author["author"]

#Class create
class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Cog listener
    @commands.Cog.listener()
    async def on_ready(self):
        print("Activity cog - Online.")

    #Activ change
    @commands.slash_command(name="activ")
    async def activity(self, ctx, type, *, name):
        if ctx.author.id in author:
            try:
                if type == "game":
                    await self.bot.change_presence(activity=disnake.Game(name=f"{name}"))
                    await ctx.send(f"Activity\nType - {type}\nName - {name}", delete_after=3)
                elif type == "watching":
                    await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.watching, name=f"{name}"))
                    await ctx.send(f"Activity\nType - {type}\nName - {name}", delete_after=3)
                elif type == "listening":
                    await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name=f"{name}"))
                    await ctx.send(f"Activity\nType - {type}\nName - {name}", delete_after=3)
                else:
                	await self.bot.change_presence(activity=None)
                	await ctx.send(f"Activity deleted", delete_after=3)
            except Exception as e:
                await ctx.send(f"Error: {e}")
        else:
            await ctx.send("You cannot use this command.")

#Setup cog file
def setup(bot):
    bot.add_cog(Activity(bot))
