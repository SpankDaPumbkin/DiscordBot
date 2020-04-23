import discord
from discord.ext import commands
BotOwner = ['51393664119957097']
class DNUL:
    def __init__(self, Bot):
        self.Bot = Bot

    async def on_ready(self):
        global msg
        msg = self.Bot.say

    @commands.command(pass_context=True)
    async def load(self,ctx, extension):
        userID = ctx.message.author.id
        if userID in BotOwner:
            try:
                self.Bot.load_extension(extension)
                print('loaded ',extension)
            except Exception as error:
               print(extension,'was not loaded ', error)
        else:
            await msg('fuck off')

    @commands.command(pass_context=True)
    async def unload(self,ctx, extension):
        userID = ctx.message.author.id
        if userID in BotOwner:
            try:
                self.Bot.unload_extension(extension)
                await msg('unloaded {}'.format(extension))
            except Exception as error:
                await msg('{} could not be unloaded [{}]'.format(extension, error))
        else:
            await msg('you cant do that')

    @commands.command(pass_context=True)
    async def TF(self,ctx):
        await msg('what do u want with them?')

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        t = await msg('Pong!')
        ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
        await msg('Took: {} ms '.format(int(ms)))
        
    @commands.command(pass_context=True)
    async def suckmydick(self,ctx):
        await msg('*blushes* ok daddy *gets on knees* are you ready? *unzips pants pulls out 16" cock* WOW SO BIG! *slowly puts mouth around your cock* slurp slurp gag gag gag sploosh. WOW DADDY! that was amazing lets do it again sometime. *gets up with some gu on my face*')

def setup(Bot):
    Bot.add_cog(DNUL(Bot))