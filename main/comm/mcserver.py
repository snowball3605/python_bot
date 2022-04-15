import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand
from mcstatus import MinecraftServer

from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

print("reload -server- done")


class Server(Cog_Extension):
    @cog_ext.cog_slash(name="Server", description="minecraft_server_search")
    async def online(self, ctx, mc_server):
        try:
            server = MinecraftServer.lookup(f"{mc_server}")
            status = server.status()
            OKL = status.players.online
            hyut = status.latency
            lo = status.version.protocol
            embed = discord.Embed(
                title=f"伺服器|server:{mc_server} \n 伺服器當前玩家在線人數|players online:{OKL} \n 伺服器延遲|server ping:{hyut} \n {lo}")
            await ctx.send(embed=embed)
        except TimeoutError:
            await ctx.send(f"沒有這個伺服器{mc_server}")
        except Exception:
            await ctx.send(f"沒有這個伺服器{mc_server}")


def setup(bot):
    bot.add_cog(Server(bot))
