import discord
from discord.ext import commands
import json
import random
import colorama
from colorama import Fore, Back, Style
import random
colorama.init()
class act:
    def __init__(self, Bot):
        self.Bot = Bot

    async def on_ready(self):
        global msg
        msg = self.Bot.say

    @commands.command(pass_context=True)
    async def atest(self,ctx,*,data):
        id = '513936641199570975'
        if ctx.message.author.id == id:
            channel = self.Bot.get_channel('624109808739680276')
            await self.Bot.send_message(channel,data)
        else:
            await self.Bot.say('fuck off')
    @commands.command(pass_context=True)
    async def smt(self,ctx):
        num = 0
        numt = 0
        total = []
        for server in self.Bot.servers:  
            print(num, 'members for', server)
            num = 0  
            print(Fore.GREEN, server, Style.RESET_ALL)
            for member in server.members:
                if member == self.Bot.user:
                    print('me')
                else:
                    num += 1
                    total.append(numt)
                    numt += 1
                    print(member)
            print(random.choice(total)) 
            ran = random.choice(total)
            sec = random.choice(total)
            if ran == sec:
                await self.Bot.say('lucky users are {} with the number {}'.format(member,ran))
            else:
                await self.Bot.say('the numbers where {} and {}'.format(ran,sec))

    @commands.command(pass_context=True)
    async def listmembers(self,ctx):
        role = discord.utils.get(ctx.message.server.roles, name="admin")
        mod = discord.utils.get(ctx.message.server.roles, name="mods")
        await self.Bot.say(role)
        num = 0
        for server in self.Bot.servers:
            for member in server.members:
                num += 1
                if role or mod in member.roles:
                    if role in member.roles:
                        if member == self.Bot.user:
                            print('me')
                        else:
                            print(member)
                            try:
                                destion = member
                                fmt = 'this is a PSA please get fucked and DM spankie if this worked thx  '
                                await self.Bot.send_message(destion, fmt)
                                print('{} is a admin'.format(member))
                            except discord.Forbidden as e:
                                print("Failed to send a message. Reason: {}".format(type(e).__name__))
                    if mod in member.roles:
                        if member == self.Bot.user:
                            print('me')
                        else:
                            print(member)
                            try:
                                destion = member
                                fmt = 'this is a PSA please get fucked and DM spankie if this worked thx  '
                                await self.Bot.send_message(destion, fmt)
                                print('{} is a mod'.format(member))
                            except discord.Forbidden as e:
                                print("Failed to send a message. Reason: {}".format(type(e).__name__))

    @commands.command(pass_context=True)
    async def unknownmem(self,ctx):
        for server in self.Bot.servers:
            print('i am apart of {}'.format(server.name))
        role = discord.utils.get(ctx.message.server.roles, name="unknown")
        await self.Bot.say(role)
        num = 0
        for server in self.Bot.servers:
            for member in server.members:
                num += 1
                if role in member.roles:
                    if role in member.roles:
                        if member == self.Bot.user:
                            print('me')
                        else:
                            print(member,'is a unknown')

    @commands.command(pass_context=True)
    async def dme(self,ctx):
        destion = ctx.message.author
        fmt = 'Welcome to If you are interested in joining the clan or ranked team please DM Onion  '
        await self.Bot.send_message(destion, fmt)

def setup(Bot):
    Bot.add_cog(act(Bot))