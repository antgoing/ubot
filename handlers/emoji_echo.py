# handlers/server_emoji_echo.py

import re
import random
from discord import Message
from discord.utils import get

# Matches <:name:id> and <a:name:id>
EMOJI_REGEX = re.compile(r'<(a?):(\w+):(\d+)>')

async def try_echo_emoji(message: Message) -> bool:
    """
    If the message contains any custom emoji that belongs to
    the current guild, echo the first one back and return True.
    Otherwise return False.
    """
    if not message.guild:
        return False

    for anim_flag, name, eid_str in EMOJI_REGEX.findall(message.content):
        emoji_id = int(eid_str)
        guild_emoji = get(message.guild.emojis, id=emoji_id)
        if guild_emoji:
            if random.randint(1, 100) == 14:
                await message.channel.send(str(guild_emoji))
                return True
            # otherwise skip echoing
            return False

    return False
