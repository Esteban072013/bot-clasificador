import discord 
from discord.ext import commands

from waste import sort_waste

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def clasificar(ctx, type_waste: str):
    
    result = sort_waste(type_waste)

    await ctx.send(result)


token = ""
bot.run(token)
