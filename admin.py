import discord
from discord.ext import commands
import json
info = {}
class admin:
	def __init__(self,Bot):
		self.Bot = Bot

	async def on_ready(self):
		global msg
		msg = self.Bot.say
		global info
		try:
			with open('info.json') as f:             
				info = json.load(f)
		except FileNotFoundError:
				print('can not load info.json')

	@commands.command(pass_context=True)
	async def peek(self,ctx, user: discord.Member=None):
		with open('info.json') as f:             
			info = json.load(f)
		id = user.name
		if id not in info:
			await msg('dam you have not been warned lets keep like that')
		woah = info[id]['warns']
		await msg('{} has {} number of warns'.format(user.mention,woah))

	@commands.command(pass_context=True)
	@commands.has_any_role("KRYptopia's king", 'admin')
	async def delete(self,ctx, user: discord.Member=None):

		id = user.name
		if id not in info:
			await msg('user is not in the system')
		else:
			info[id]['warns'] = 0
			await self.save()
			await msg('task finished {} has {} warns'.format(id,info[id]['warns']))

	@commands.command(pass_context=True)
	@commands.has_any_role("KRYptopia's king", 'admin')
	async def warn(self,ctx, user: discord.Member=None):
		id = user.name
		await msg('hey stop that {}'.format(user.mention))
		if id not in info:
			await self.makeC(id)
		else:
			info[id]['warns'] += 1
			await self.save()
    
	async def makeC(self,id):
		info[id] = {}
		info[id]['warns'] = 1
		info[id]['bans'] = 0
		await self.save()

	async def save(self):
		with open('info.json', 'w+') as f:
			json.dump(info, f,indent=4)

def setup(Bot):
	Bot.add_cog(admin(Bot))