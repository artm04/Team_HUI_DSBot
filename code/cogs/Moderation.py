#Imports
from disnake.ext import commands
import disnake


last_messages = {}

#Class create
class Moderation(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	#Cog listener
	@commands.Cog.listener()
	async def on_ready(self):
		print("Moderation cog - Online.")
		
	#Cog listener on_message
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id in last_messages:
			if message.content == last_messages[message.author.id].content:
				await message.delete()
				return
			
		last_messages[message.author.id] = message
		
		await self.bot.process_commands(message)
	
#Setup cog filel
def setup(bot):
	bot.add_cog(Moderation(bot))
