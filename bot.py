import os
import discord
from dotenv import load_dotenv
from handlers.channel_u import try_handle_u_channel
from handlers.emoji_echo import try_echo_emoji

load_dotenv()
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("no TOKEN in .env file")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Zalogowano jako {client.user}")
    '''CHANNEL_ID = 890378481077202958
    ch = client.get_channel(CHANNEL_ID)
    if ch:
        await ch.send("bla") xd'''

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if await try_handle_u_channel(message):
        return
    
    if await try_echo_emoji(message):
        return

client.run(TOKEN)
