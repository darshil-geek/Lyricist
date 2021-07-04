import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def ping(ctx):
    await ctx.channel.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.channel.send('Konichiwa!')

bot.run('INSERT TOKEN HERE')