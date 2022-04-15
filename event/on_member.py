import discord
from discord.ext import commands
from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select
from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

print("reload -onmember- done")


class onmember(Cog_Extension):

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f"{member} leave")
        guilds = member.guild
        channel1 = self.bot.get_channel(946364391492825098)
        await channel1.edit(name=f"🔴人數|Member:{guilds.member_count}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"{member}  join!")
        role1 = discord.utils.get(member.guild.roles, name="驗證-verify")
        await member.add_roles(role1)
        guilds = member.guild
        channel1 = self.bot.get_channel(946364391492825098)
        role = discord.utils.get(member.guild.roles, name="players")
        await member.add_roles(role)
        await channel1.edit(name=f"🔴人數|Member:{guilds.member_count}")


def setup(bot):
    bot.add_cog(onmember(bot))
