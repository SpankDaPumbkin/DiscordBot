import discord
from discord.ext import commands
import json
import random
pets = {}
class petsys:
    def __init__(self, Bot):
        self.Bot = Bot

    async def on_ready(self):
	    global pets
	    try:
		    with open('petinfo.json') as f:             
		    	pets = json.load(f)
	    except FileNotFoundError:
	    	print('could not load money.json')
	    	pets = {}

    @commands.command(pass_context=True)
    async def catch(self,ctx,Type=None):
        if not Type:
            await self.Bot.say('please specify what type u are: water, earth,wind,fire')
        id = ctx.message.author.name
        if Type == "water":
            if id not in pets["water"]:
                if id in pets["fire"]:
                    await self.Bot.say("you are already part of a Type")
                else:
                    if id in pets["wind"]:
                        await self.Bot.say("you are already part of a Type")
                    else:
                        if id in pets["earth"]:
                            await self.Bot.say("you are already part of a Type")
                        else:

                            pets["water"][id] = {}
                            pets["water"][id]["stats"] = {}
                            pets["water"][id]["stats"]["HP"] = 100
                            pets["water"][id]["stats"]["ATK"] = 10
                            pets["water"][id]["stats"]["SPD"] = 10
                            pets["water"][id]["stats"]["INT"] = 10
                            await self.Bot.say("You are now registered as a water element")
                            await self.save()
            else:
                await self.Bot.say("you are already part of this type")
        if Type == "fire":
            if id not in pets["fire"]:
                if id in pets["water"]:
                    await self.Bot.say("you are already part of a Type")
                else:
                    if id in pets["wind"]:
                        await self.Bot.say("you are already part of a Type")
                    else:
                        if id in pets["earth"]:
                            await self.Bot.say("you are already part of a Type")
                        else:

                            pets["fire"][id] = {}
                            pets["fire"][id]["stats"] = {}
                            pets["fire"][id]["stats"]["HP"] = 100
                            pets["fire"][id]["stats"]["ATK"] = 20
                            pets["fire"][id]["stats"]["SPD"] = 10
                            pets["fire"][id]["stats"]["INT"] = 5
                            await self.Bot.say("You are now registered as a water element")
                            await self.save()
            else:
                await self.Bot.say("you are already part of this type")
        if Type == "wind":
            if id not in pets["wind"]:
                if id in pets["fire"]:
                    await self.Bot.say("you are already part of a Type")
                else:
                    if id in pets["water"]:
                        await self.Bot.say("you are already part of a Type")
                    else:
                        if id in pets["earth"]:
                            await self.Bot.say("you are already part of a Type")
                        else:

                            pets["wind"][id] = {}
                            pets["wind"][id]["stats"] = {}
                            pets["wind"][id]["stats"]["HP"] = 100
                            pets["wind"][id]["stats"]["ATK"] = 510
                            pets["wind"][id]["stats"]["SPD"] = 10
                            pets["wind"][id]["stats"]["INT"] = 5
                            await self.Bot.say("You are now registered as a water element")
                            await self.save()
            else:
                await self.Bot.say("you are already part of this type")
        if Type == "earth":
            if id not in pets["earth"]:
                if id in pets["fire"]:
                    await self.Bot.say("you are already part of a Type")
                else:
                    if id in pets["wind"]:
                        await self.Bot.say("you are already part of a Type")
                    else:
                        if id in pets["water"]:
                            await self.Bot.say("you are already part of a Type")
                        else:

                            pets["earth"][id] = {}
                            pets["earth"][id]["stats"] = {}
                            pets["earth"][id]["stats"]["HP"] = 200
                            pets["earth"][id]["stats"]["ATK"] = 10
                            pets["earth"][id]["stats"]["SPD"] = 5
                            pets["earth"][id]["stats"]["INT"] = 5
                            await self.Bot.say("You are now registered as a water element")
                            await self.save()
            else:
                await self.Bot.say("you are already part of this type")

    async def save(self):
        with open('petinfo.json', 'w+') as f:
            json.dump(pets, f,indent=4)
	
    @commands.command(pass_context=True)
    async def testcmd(self,ctx):
        await self.Bot.say(pets)
        id = ctx.message.author.name
        Typsus = "water","earth","wind","fire"
        if id in pets[Typsus]:
            await self.Bot.say('yes')
        else:
            await self.Bot.say('no')





def setup(Bot):
    Bot.add_cog(petsys(Bot))