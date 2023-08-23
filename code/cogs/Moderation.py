#Imports
from disnake.ext import commands
import disnake
import json

with open('../config.json') as f:
	banwords = json.load(f)


#Last message var.
last_messages = {}
#Ban Words var.
banwords_var = []

#Class create
class Moderation(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	#Cog listener on_ready
	@commands.Cog.listener()
	async def on_ready(self):
		print("Moderation cog - Online.")
		
	#Cog listener on_message
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id in last_messages:
			if message.content == last_messages[message.author.id].content:
				await message.delete()
				pass
			
		last_messages[message.author.id] = message
		
		await self.bot.process_commands(message)

	# Cog listener on_message again
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author.id in last_messages:
			if message.content == banwords_var[message.author.id].content:
				await message.delete()
				pass

		await self.bot.process_commands(message)


	for banwords_var in banwords:

	
#Setup cog file
def setup(bot):
	bot.add_cog(Moderation(bot))
