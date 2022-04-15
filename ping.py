import discord
from discord.ext import commands
from discord_slash import SlashCommand, cog_ext

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

print("reload -ping- done")


class ping(Cog_Extension):

    @cog_ext.cog_slash(description="ping")
    async def ping(self, ctx):
        embed = discord.Embed(title=f'ping|延遲:{round(self.bot.latency * 150)}ms')
        await ctx.send(embed=embed)


def setup(self):
    bot.add_cog(ping(bot))
