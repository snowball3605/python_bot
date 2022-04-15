from datetime import datetime
import requests
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)


class blacklist(Cog_Extension):
    @cog_ext.cog_slash(name="blacklist", description="[mc_name] [ip] [reason] [why]")
    @commands.has_permissions(administrator=True)
    async def addblacklist(self, ctx, name, ip, reason, why):
        url = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}?").json()
        id = url['id']
        now = datetime.now()
        c_t = now.strftime("%H:%M:%S")
        embed = discord.Embed(title=f"MC_NAME = {name}",
                              description=f"IP = {ip} \n reason = {reason} \n UUID = {id} \n ban_time = {c_t} \n 加入{why}",
                              colour=0xF50A60)
        feafwa = f"[MC_NAME = {name} \n IP = {ip} \n reason = {reason} \n UUID = {id} \n Ban_time = {c_t} \n 加入{why} \n ---------------------------------------------------------------------------]"
        await ctx.send(embed=embed)
        with open('./blacklist.txt', 'a') as file:
            file.write(feafwa + '\n')


def setup(bot):
    bot.add_cog(blacklist(bot))
