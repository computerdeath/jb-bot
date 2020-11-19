import discord

token_file = open('TOKEN.key', 'r')
TOKEN = token_file.read().strip()
token_file.close()
client=discord.Client(status="TINK TINK TINK")

@client.event
async def on_ready():
    print("The bot is ready!")
    game = discord.Game("TINK TINK TINK")
    await client.change_presence(status=discord.Status.idle, activity=game)
@client.event
async def on_message(message):
    if message.author.bot:
        return
    hold = message.content
    if "you people" in hold.lower():
        await message.channel.send("what do you mean YOU PEOPLE")
        hold = ""



client.run(TOKEN)