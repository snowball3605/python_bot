import asyncio

import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

print('Reload -timer- done')


class time1(Cog_Extension):

    @cog_ext.cog_slash(name="Timer", description="timer")
    async def time(self, ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 1000000:
                await ctx.send("時間不能超過1000秒也不能低於零秒")
                raise BaseException
            if secondint <= 0:
                await ctx.send("時間不能超過1000秒也不能低於零秒")
                raise BaseException

            yyds = await ctx.send(f"剩餘時間: {seconds}")

            while True:
                secondint -= 1
                if secondint == 0:
                    await yyds.edit(content="時間結束!!!")
                    break

                await yyds.edit(content=f"剩餘時間: {secondint}")
                await asyncio.sleep(1)
        except ValueError:
            await ctx.send("計時出現故障")


def setup(bot):
    bot.add_cog(time1(bot))
