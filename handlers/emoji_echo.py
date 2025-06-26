import re
import random
from discord import Message
from discord.utils import get

EMOJI_REGEX = re.compile(r'<(a?):(\w+):(\d+)>')

async def try_echo_emoji(message: Message) -> bool:
    if not message.guild:
        return False
    
    valid_emojis = [
        get(message.guild.emojis, id=int(eid))
        for _, _, eid in EMOJI_REGEX.findall(message.content)
        if get(message.guild.emojis, id=int(eid))
    ]

    if valid_emojis and random.randint(1, 100) <= 11:
        await message.channel.send(str(random.choice(valid_emojis)))
        return True

    if message.stickers:
        sticker = message.stickers[0]
        guild_sticker = get(message.guild.stickers, id=sticker.id)
        if guild_sticker and random.randint(1, 100) <= 20:
            await message.channel.send(stickers=[guild_sticker])
            return True

    return False
