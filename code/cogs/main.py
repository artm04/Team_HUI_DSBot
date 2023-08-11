#imports
from disnake.ext import commands
import disnake


#create class
class main(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	#cog listener to print status in terminal
	@commands.Cog.listener()
	async def on_ready(self):
		print('main cog - ACTIVATED\n')

	#help command
	@commands.slash_command(name='help', description='help command')
	async def help(self, ctx):
		embed = disnake.Embed(
			title='Commands:',
			description='help - output it message;\n',
			color=disnake.Colour.lighter_gray()
			)
		await ctx.send(embed=embed)

#setup cog file
def setup(bot):
	bot.add_cog(main(bot)
