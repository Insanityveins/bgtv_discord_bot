import discord
from typing import Optional
from datetime import datetime

def embed_builder(title: str, description: str, color: discord.Color, author: Optional[discord.Member] = None, member: Optional[discord.Member] = None, user: Optional[discord.User] = None) -> discord.Embed:
    embed = discord.Embed(title=title, description=description, color=color)

    if member is not None:
        embed.set_author(name=member.name, icon_url=member.avatar)
        embed.set_footer(text=f"ID: {member.id}")

    if author is not None:
        embed.set_author(name=author.name, icon_url=author.avatar)
        embed.set_footer(text=f"ID: {author.id}")

    if user is not None:
        embed.set_author(name=user.name, icon_url=user.avatar)
        embed.set_footer(text=f"ID: {user.id}")

    embed.timestamp = datetime.now()
    return embed

def get_logging_channel(guild: discord.Guild, channel_name: str) -> discord.TextChannel:
    
    for channel in guild.text_channels:
        if channel.name == channel_name:
            return channel
        
    return None
