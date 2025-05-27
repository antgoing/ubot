import random
from discord import Message
from discord.utils import get

async def try_handle_u_channel(message: Message) -> bool:
    
    if message.channel.name != 'u':
        return False
    if 'u' not in message.content.lower():
        return False

    roll = random.random()
    if roll <   0.10:
        await message.channel.send('u')
    elif roll < 0.15:
        sticker = get(message.guild.stickers, id=914511952540225596)
        await message.channel.send(stickers=[sticker])
    elif roll < 0.16:
        emoji = get(message.guild.emojis, id=1340455055383461988)
        await message.channel.send(str(emoji))
    elif roll < 0.161:
        await message.channel.send('SUPA RARE U')
    elif roll < 0.160001:
        await message.channel.send('one in a million U <@273452094739054592>')
    else:
        return False

    return True