import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Konichiwa!!')
    if message.content.startswith('How are you'):
        await message.channel.send('I am doing fine. Hope you are doing well too')

client.run('ODYwMTc1MjUxNTU5MDIyNjUy.YN3aoQ.MU11iZQmNl7tHjVj0mEXsf_-i9Q')
