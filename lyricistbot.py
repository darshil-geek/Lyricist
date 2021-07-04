import discord
import lyricsgenius as genius
import config

api = genius.Genius('')
api = genius.Genius(config.GENIUS_TOKEN)

from discord.ext import commands
from discord.ext.commands import Bot

TOKEN = ''
TOKEN = config.BOT_TOKEN

client = commands.Bot(command_prefix = '-')
@client.event
async def on_ready():
  print('Bot is ready!')

@client.command()
async def Hi(ctx):
    await ctx.channel.send("What's up!")

@client.command()
async def lyr(ctx, *arg):
  string = ''
  a=''
  s=''
  string = arg
  for str in string:
    if(str == '~'):
      break
    a = a + " " + str

  a

  s_ = string[string.index('~') : len(string)]
  for _s in s_ :
    if(_s == '~'):
      continue
    s = s + " " + _s

  s
  await ctx.channel.send("Searching for the lyrics to {} by {} ...".format(s, a))
  song = api.search_song(s, a)
  if song:
      url = song.url
      await ctx.channel.send("Here's a link to the annotated lyrics: \n{}".format(url))
      lyrics = song.lyrics.split("\n")
      for line in lyrics:
          if line == '':
            lyrics.remove(line)
          else:
            await ctx.channel.send("{}".format(line))
      #await ctx.channel.send("Here's a link to the annotated lyrics: \n{}".format(lyrics))
  else:
        await ctx.channel.send("I was unable to find the queried song. My apologies :(  " +
        "Check for typos and try again.")

client.run(TOKEN)