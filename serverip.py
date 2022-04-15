import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)


class ServerIP(Cog_Extension):

    @cog_ext.cog_slash(name="IP", description="serverIP")
    async def ServerIP(self, ctx):
        embed = discord.Embed(title="nrts.ddns.net")
        await ctx.send(embed=embed)


def setup(self):
    bot.add_cog(ServerIP(bot))