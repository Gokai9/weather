from discord.ext import commands
import discord


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot("+", intents=intents)


@bot.event
async def on_ready():
    print("bot has ready")

bot.load_extension("commandsgroup")

bot.run('OTA2MTAyNTA0Mjg1MTUxMjcy.YYTvtw.GPuf_0znj-aVASikHkpb1eXzOcA')
