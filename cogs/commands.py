import discord
from discord.ext import commands
import asyncio
from time import sleep

class Greeting(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def ping(self, ctx):
        await ctx.respond(f"Latency is {self.bot.latency:.2f}s")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} is ready and online!")
        # channel = self.bot.get_channel(1083615587164487813)
        # await channel.send('已上線')
        # await self.on_testing()

    # async def on_testing(self):
    #     while True:
    #         print("testing")
    #         sleep(5)

def setup(bot):
    bot.add_cog(Greeting(bot))

