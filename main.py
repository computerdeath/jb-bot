import discord

token_file = open('TOKEN.key', 'r')
TOKEN = token_file.read().strip()
token_file.close()
client=discord.Client()

@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="TINK TINK TINK"))

@client.event
async def on_message(message):
    if "you people" in message.content:
        await message.channel.send("what do you mean YOU PEOPLE")



client.run(TOKEN)