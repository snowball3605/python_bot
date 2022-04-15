import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand
import random

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)


class lucky(Cog_Extension):
    @cog_ext.cog_slash(name="random number", description="[ctx]")
    async def lucky(self, ctx):
        n = 0
        while True:
            r = random.randint(1, 100)
            n += 1
            await ctx.send(r)
            if n == 1:
                await ctx.edit(r)
                if n == 100:
                    break


def setup(self):
    bot.add_cog(lucky(bot))