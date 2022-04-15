import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

print("reload -test- done")


class test(Cog_Extension):

    @cog_ext.cog_slash(description="test")
    async def test(self, ctx):
        while True:
            channel = bot.get_channel(898784993873100871)
            myid = '<@825203834455588866>'
            await channel.send_message(f"{myid}警告!")


def setup(self):
    bot.add_cog(test(bot))
