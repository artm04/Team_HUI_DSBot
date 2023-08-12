#Imports
import disnake
from disnake.ext import commands
import asyncio


#Class create
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Cog listener
    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin cog - Online.")

    #Clear chat
    @commands.has_permissions(manage_messages=True)
    @commands.command(name="clear")
    async def clear_command(self, ctx, amount: int):
        try:
            channel = ctx.channel
            messages = await channel.history(limit=amount+1).flatten()
            await channel.delete_messages(messages)
        except Exception as e:
        	await ctx.send(f"Error: {e}")

    #Kick members
    @commands.has_permissions(kick_members=True)
    @commands.slash_command(name="kick", description="Kick member")
    async def kick(self, ctx, member: disnake.Member, reason="You have been excluded."):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"User {member} excluded, reason: {reason}", delete_after=10)
        except Exception as e:
           	await ctx.send(f"Error: {e}")

    #Ban members
    @commands.has_permissions(manage_member=True)
    @commands.command(name="ban", description="Ban member")
    async def ban(self, ctx, member: disnake.Member, reason="You have been ban."):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"User {member} ban, reason: {reason}", delete_after=10)
        except Exception as e:
            await ctx.send(f"Error: {e}")

#Setup cog file
def setup(bot):
    bot.add_cog(Admin(bot))
