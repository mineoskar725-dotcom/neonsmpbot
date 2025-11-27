import discord
from discord.ext import commands
import os  # do pobrania tokena z Railway

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Pobieramy token z environment variable DISCORD_TOKEN
bot.run(os.environ["DISCORD_TOKEN"])
