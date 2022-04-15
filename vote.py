import asyncio

import discord
from discord.ext import commands
from discord_slash import cog_ext

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

print("reload -Vote- done")


class vote(Cog_Extension):

    @cog_ext.cog_slash(name="vote")
    async def vote(self, ctx, *, message, A1):
        print(message)
        embed = discord.Embed(title=f"{message} \n {A1}")
        msg = await ctx.channel.send(embed=embed)
        one = await msg.add_reaction('🇦')
        two = await msg.add_reaction('🇧')
        tre = await msg.add_reaction('🇨')
        WTF = await msg.add_reaction('🇩')
        try:
            secondint = 10
            seconds = 10
            if secondint > 1000:
                await ctx.send("jnra")
                raise BaseException
            if secondint <= 0:
                await ctx.send("grb")
                raise BaseException

            messsage = await ctx.send(f"投票餘下時間: {seconds}")

            while True:
                secondint -= 1
                if secondint == 0:
                    await messsage.edit(content="投票結束!宣佈結果")
                    await ctx.send(f"A={one}  B={two}  C={tre}  D={WTF}")
                    break

                await messsage.edit(content=f"投票餘下時間: {secondint}")
                await asyncio.sleep(1)
        except ValueError:
            await ctx.send("hfagj")


def setup(self):
    bot.add_cog(vote(bot))
