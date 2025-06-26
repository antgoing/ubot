import os
import discord
from dotenv import load_dotenv
from handlers.channel_u import try_handle_u_channel
from handlers.emoji_echo import try_echo_emoji
from handlers.random_reaction import try_random_reaction

load_dotenv()
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("no TOKEN in .env file")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TARGET_REACTION_CHANNEL_IDS = [890378481077202958, 903309776539250710, 903310093364396072, 903306416822030346, 903310225522696274, 903309701217927179, 1312156580506239079, 1312457182893310024, 1349756891554775161, 983426109364396042, 908382362755268638, 1043292223451697153, 903386664410419201, 903310345072951308] # ZASTĄP SWOIMI ID KANAŁÓW!

@client.event
async def on_ready():
    print(f"Zalogowano jako {client.user}")
    CHANNEL_ID = 890378481077202958
    ch = client.get_channel(CHANNEL_ID)
    if ch:
        await ch.send("ok")

@client.event
async def on_message(message):
    if await try_handle_u_channel(message):
        return
    
    if await try_echo_emoji(message):
        return
    
    if await try_random_reaction(message, TARGET_REACTION_CHANNEL_IDS):
        return

client.run(TOKEN)
