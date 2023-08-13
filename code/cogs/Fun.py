#Imports
import disnake
from disnake.ext import commands
import random
from random import randint


#Class create
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Cog listener
    @commands.Cog.listener()
    async def on_ready(self):
        print("Fun cog - Online.")

    #Dice
    @commands.slash_command(name="dice", description="Outputs a random value from 1 to 6.")
    async def dice(ctx):
    	await ctx.send(randint(1, 6))

    #DicePlus
    @commands.slash_command(name="diceplus", description="Outputs a random value from 1 to 20.")
    async def dice(ctx):
    	await ctx.send(randint(1, 20))

    #Roll
    @commands.slash_command(name="roll", description="Outputs a random value from 1 to 100.")
    async def roll(ctx):
    	await ctx.send(randint(1, 100))

    #FlipCyberCoin
    @commands.slash_command(name="flipcybercoin", aliases=["fcc"], description="Output random value from 0 to 1")
    async def fcc(ctx):
    	await ctx.send(randint(0, 1))

    #Magicball
    @commands.slash_command(name="magicball", description="Output random answer, like yes, no, etc.")
    async def magicball(ctx, *, question):
    	responses = [
    	"Yes",
    	"No",
    	"Perhaps",
    	"IDK",
    	"Very doubtful",
    	"Undoubtedly",
    	"Of course",
    	"It's not clear yet, try again"]
    	
    	response = random.choice(responses)
    	await ctx.send(f"Question – {question}\nAnswer - {response}")

    #Custom randint
    @commands.slash_command()
    async def randint(self, ctx, start: int, end: int):
    	await ctx.send(randint(start, end))

    #User Avatar
    @commands.slash_command()
    async def avatar(self, ctx, member: disnake.Member = None):
        member = member or ctx.author
        if member is not None:
            avatar_url = member.avatar.url if member is not None else ""
            await ctx.send(member.avatar.url)
        else:
            await ctx.send("The participant's avatar could not be retrieved.")
        
#Setup cog file
def setup(bot):
    bot.add_cog(Fun(bot))
