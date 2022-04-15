import time

import discord
from discord.ext import commands

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


class onready(Cog_Extension):

    @commands.Cog.listener()
    async def on_ready(self):
        ac = discord.Game(name='Python', type=3)
        await self.bot.change_presence(status=discord.Status.idle, activity=ac)
        print("reload -Bot- done")
        time.sleep(2)
        print("reload -ALL- done")


def setup():
    bot.add_cog(onready(bot))
