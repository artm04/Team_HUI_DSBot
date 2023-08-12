#Imports
import disnake
from disnake.ext import commands
import datetime

#Class create
class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Cog listener
    @commands.Cog.listener()
    async def on_ready(self):
        print("Main cog - Online.")

    #Ping
    @commands.slash_command()
    async def ping(self, ctx):
    	await ctx.send("Pong.")

    @commands.slash_command(description="Help command.")
    async def help(self, ctx):
        #HELP Embed
        embed = disnake.Embed(
            title = "commands:",
            description="Help - Show all commands.\nInfo - Show info adout Team H.U.I.\n\nDice - Outputs a random value from 1 to 6.\nRoll - Outputs a random value from 1 to 100.\nFlipCyberCoin(fcc) - Output random value from 0 to 1\nMagicball - Output random answer, like yes, no, etc.",
            color=disnake.Colour.lighter_gray(),
        timestamp=datetime.datetime.now(),
        )
        embed.set_author(
            name="",
            url="",
            icon_url="",
        )
        embed.set_footer(
        text="",
        icon_url="",
        )
        embed.set_thumbnail(url="")
        embed.set_image(url="")
        
        await ctx.send(embed=embed)

    @commands.slash_command(description="Info adout Team H.U.I.")
    async def teaminfo(self, ctx):
        #INFO Embed
        embed = disnake.Embed(
            title = "Info adout Team H.U.I.",
            description="Team H.U.I. was invented and created on October 19, 2022 at the moment there are 3 participants in the team, 2 of them are working on VFX and one on Chart.",
            color=disnake.Colour.lighter_gray(),
        timestamp=datetime.datetime.now(),
        )
        embed.set_author(
            name="Team H.U.I.",
            url="https://discord.gg/C2Qgn95FCu",
            icon_url="https://media.discordapp.net/attachments/1116570284632318082/1116570404048338954/Team_H.U.I..png?format=png",
        )
        embed.set_thumbnail(url="")
        embed.set_image(url="")
        
        await ctx.send(embed=embed)

#Setup cog file
def setup(bot):
    bot.add_cog(Main(bot))
	
