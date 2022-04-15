import discord
import requests
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)


class players(Cog_Extension):
    @cog_ext.cog_slash(name="players", description="minecraft_players_search")
    async def players(self, ctx, player):
        try:
            url = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{player}?").json()
            id = url['id']
            embed = discord.Embed(title=f"Name:{player} \n ID:{id}")
            await ctx.send(embed=embed)
        except ValueError:
            embed = discord.Embed(title=f"沒有這位{player}玩家")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(players(bot))
