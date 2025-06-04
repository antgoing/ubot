import random
from discord import Message
from typing import List

async def try_random_reaction(message: Message, target_channel_ids: List[int]) -> bool:
    """
    Attempts to add a random custom emoji reaction to the message
    with a 10% chance if the message is in one of the target channels.
    Returns True if a reaction was attempted (regardless of success), False otherwise.
    """
    if not message.guild:
        return False

    # Check if the message is from one of the target channels
    if message.channel.id not in target_channel_ids:
        return False

    # 10% chance to react
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
                return True # We attempted to react, so return True
        else:
            print(f'Brak emotek na serwerze {message.guild.name} do zareagowania.')
            return False # No emojis to react with, so no attempt was made
    
    return False # No reaction due to random chance