from datetime import datetime

import discord
from discord.ext import commands

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

print("reload -on_message- done")


class onmessage(Cog_Extension):

    @commands.Cog.listener()
    async def on_message(self, msg):

        if msg.channel.id != 953659969788575765 and msg.channel.id != 897447243907477525 and msg.channel.id != 943522634958766110 and msg.channel.id != 959094123003015178 and msg.channel.id != 959082794141769748:
            try:
                now = datetime.now()
                c_t = now.strftime("%H:%M:%S")
                if msg.guild.id == 825162735603810316:
                    channel1 = self.bot.get_channel(946364391492825098)
                    await channel1.edit(name=f"🔴人數|Member:{msg.guild.member_count}")
                channel = self.bot.get_channel(953659969788575765)
                print(msg)
                message = msg.content
                ak = msg.channel.name
                member = msg.author.name
                mem = msg.author.discriminator
                guild = msg.guild.name
                embed = discord.Embed(title=f"{member}#{mem} 🟡 {c_t}", description=f'{message}')
                embed.add_field(name=f"{guild} 🟠 {ak}", value=f"{msg.id}")
                await channel.send(embed=embed)
            except Exception:
                pass
        else:
            pass


def setup(self):
    bot.add_cog(onmessage(bot))
