# Bot by SpankDaPumbkin
me = '513936641199570975'
# {
import discord  
from discord.ext import commands
from discord.ext.commands import Bot # } --> for discord ig
import json # for my config file
import asyncio # async ig
import random # something random
from colorama import Fore, Back, Style # to add color

with open('config.json') as g:             
    config = json.load(g)

Bot = commands.Bot(command_prefix= config['prefix']) # i dont know how to describe it
Bot.remove_command('help') # i dont like the default help
# this command is not really needed it is super helpful to know when the bot is fully on and working 
@Bot.event
async def on_ready():    
    c = [Fore.GREEN,Fore.BLUE,Fore.RED,Fore.CYAN,Fore.MAGENTA]
    randomc = (random.choice(c))
    print(randomc)
    reset = Style.RESET_ALL
    await Bot.change_presence(game=discord.Game(name='V1.1'))
    #print(Fore.GREEN, server, Style.RESET_ALL)
    print((random.choice(c)),'my Bot name is ',config['bot_name'], reset)
    print((random.choice(c)),'my id is ', config['bot_id'], reset)
    print((random.choice(c)),'the discord api version is ',discord.__version__, reset)
    print((random.choice(c)),'my name and # is',Bot.user,reset)
    print ((random.choice(c)),"I am fully ready for you master ham",reset)
    print((random.choice(c)),'============================================================================',reset)

# DO NOT DELETE    
#----------------------------------------------------------------------
@Bot.command(pass_context=True)
async def Bload(ctx:None, extension):
    id = ctx.message.author.id
    if id == me:
        try:
            Bot.load_extension(extension)
            await Bot.say('loaded {}'.format(extension))
        except Exception as error:
            print('{} could not be loaded [{}]'.format(extension, error))

if __name__ == '__main__':
    for extension in config['extensions']:
        try:
            Bot.load_extension(extension)
            #print(extension,'is ready for use')
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))
# ---------------------------------------------------------------------
Bot.run(config['token']) 