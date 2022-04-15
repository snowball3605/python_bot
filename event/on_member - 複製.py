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
        embed1 = discord.Embed(title="歡迎加入NRTS伺服器")
        embed = discord.Embed(title="你是否會遵守並服從管理員指引 \nWill you follow and obey the administrator's guidelines?")
        embed2 = discord.Embed(title="你曾經或現在是否有遊玩過minecraft \nHave you ever played minecraft?")
        embed3 = discord.Embed(title="你不想遵守也要遵守 \nYou don't want to obey, but you have to obey")
        await member.send(embed=embed, components=[
            [Button(label="是|Yes", style="3", custom_id="button1"), Button(label="否|No", style="3", custom_id="button2")]
            ])
        inte = await self.bot.wait_for("button_click", check=lambda i: i.custom_id == "button1")
        inte2 = await self.bot.wait_for("button_click", check=lambda i: i.custom_id == "button2")

        await inte.send(embed=embed2, components=[
            [Button(label="有|Yes", style="3", custom_id="button3"), Button(label="否|No", style="3", custom_id="button4")]
        ])
        intee2 = await self.bot.wait_for("button_click", check=lambda i: i.custom_id == "button3")
        await inte2.send(embed=embed3)
        int2 = await self.bot.wait_for("button_click", check=lambda i: i.custom_id == "button4")
        await int2.send(content=embed1)
        await intee2.send(content=embed1)
        guilds = member.guild
        channel1 = self.bot.get_channel(946364391492825098)
        role = discord.utils.get(member.guild.roles, name="players")
        await member.add_roles(role)
        await channel1.edit(name=f"🔴人數|Member:{guilds.member_count}")


def setup(bot):
    bot.add_cog(onmember(bot))
