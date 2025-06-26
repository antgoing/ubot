import random
from discord import Message
from typing import List

async def try_random_reaction(message: Message, target_channel_ids: List[int]) -> bool:
    if not message.guild:
        return False

    if message.channel.id not in target_channel_ids:
        return False

    if random.random() < 0.02:
        guild_emojis = message.guild.emojis
        if guild_emojis:
            random_emoji = random.choice(guild_emojis)
            try:
                await message.add_reaction(random_emoji)
                print(f'Reacted {random_emoji.name} in {message.channel.name}')
                return True
            except Exception as e:
                print(f'Nie udało się dodać reakcji: {e}')
                return True 
        else:
            print(f'Brak emotek na serwerze {message.guild.name} do zareagowania.')
            return False 
    return False 