from discord.ext import commands
import discord
import time
from datetime import datetime
import api
import math


class CommandsGroup(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.message = None

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.message = message
        print(message)

    @commands.command(name="last")
    async def lastmsg(self, ctx: commands.Context):
        if self.message == None:
            await ctx.send("Message not found")
            return
        author = self.message.author
        content = self.message.content
        embed = discord.Embed(
            title=f"Message from {author}", description=content, timestamp=datetime.utcnow())
        embed.add_field(name="line 1", value="content for line 1", inline=True)
        embed.set_author(
            name=author, icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")
        embed.set_footer(text="this is a footer")
        await ctx.send(embed=embed)

    @commands.command("ping")
    async def ping(self, ctx: commands.Context):
        start = time.time()
        pesan = await ctx.send("test ping...")
        end = time.time()
        await pesan.edit(content=f"ping => {round(self.bot.latency*1000)} ms \n api => {round((end-start)*1000)} ms")

    @commands.command(name="weather")
    async def weather(self, ctx: commands.Context, city):
        res = api.cityname(city)
        embed = discord.Embed(
            title=f"Weather in {res['name']}", description=f"Temperature {math.floor(res['main']['temp'])} C")
        embed.add_field(
            name=f"Weather {res['weather'][0]['main']}", value=f"{res['weather'][0]['description']}")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(CommandsGroup(bot))
