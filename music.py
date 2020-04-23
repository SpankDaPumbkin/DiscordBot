import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import os
import urllib.parse, urllib.request, re
import webbrowser
import youtube_dl

players = {}
class music:
    def __init__(self, Bot):
        self.Bot = Bot




    @commands.command(pass_context=True)
    async def play(self,ctx,link):
        server = ctx.message.server
        voice_client = self.Bot.voice_client_in(server)
        player = await voice_client.create_ytdl_player(link)
        players[server.id] = player
        player.start()

    @commands.command(pass_context=True)
    async def joincall(self,ctx):
        channeltojoin = ctx.message.author.voice.voice_channel
        await self.Bot.join_voice_channel(channeltojoin)

    @commands.command(pass_context=True)
    async def musictest(self,ctx, *, jcn):
        for channel in self.Bot.get_all_channels():
            if channel.name == jcn:
                await self.Bot.say('i found it! is it {}? '.format(channel.name))
                if channel.type == discord.ChannelType.voice:
                    #joinchannel = channel.name
                    await self.Bot.say(channel.name)
                    await self.Bot.say(channel.type)
                    await self.Bot.say(channel.id)
                    await self.Bot.say(channel)
                    voice = await self.Bot.join_voice_channel(channel)
                    player = await voice.create_ytdl_player('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                    player.start()
                    return
                else:
                    await self.Bot.say('this is a text channel sorry')
                    return

def setup(Bot):
    Bot.add_cog(music(Bot))