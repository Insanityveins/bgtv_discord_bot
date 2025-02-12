import discord
from dotenv import load_dotenv
import os

from utils.utils import embed_builder, get_logging_channel


LOG_CHANNEL_NAME = "logs🌴"
RED = discord.Color.red()
ORANGE = discord.Color.orange()
GREEN = discord.Color.green()


class CustomBot(discord.Client):

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        
    async def on_message_delete(self, message: discord.Message):
        logging_channel = get_logging_channel(message.guild, LOG_CHANNEL_NAME)

        title = "Member deleted a message"
        description = f"**{message.author.name}** deleted a message"
        embed = embed_builder(title=title, description=description, color=RED, author=message.author)
        embed.add_field(name="Message Deleted:", value=message.content)
        await logging_channel.send(embed=embed)


    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        logging_channel = get_logging_channel(before.guild, LOG_CHANNEL_NAME)

        title = "Member edited a message"
        description = f"**{before.author.name}** edited a message"
        embed = embed_builder(title=title, description=description, color=ORANGE, author=before.author)
        embed.add_field(name="Message Before:", value=before.content, inline=False)
        embed.add_field(name="Message After:", value=after.content, inline=False)
        await logging_channel.send(embed=embed)


    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        logging_channel = get_logging_channel(member.guild, LOG_CHANNEL_NAME)

        # check for situations differing between joining, leaving, and moving vcs
        embed: discord.Embed = None

        # just joined a vc
        if before.channel is None and after.channel is not None:
            title = "Member joined a voice channel"
            description = f"**{member.name}** joined {after.channel.name}"
            embed = embed_builder(title=title, description=description, color=GREEN, member=member)

        # just left a vc
        if before.channel is not None and after.channel is None:
            title = "Member left a voice channel"
            description = f"**{member.name}** left {before.channel.name}"
            embed = embed_builder(title=title, description=description, color=RED, member=member)

        # moved vcs
        if before.channel is not None and after.channel is not None:
            title = "Member moved voice channels"
            description = f"**{member.name}** moved voice channels"
            embed = embed_builder(title=title, description=description, color=ORANGE, member=member)
            embed.add_field(name="OLD VC", value=before.channel.name)
            embed.add_field(name="NEW VC", value=after.channel.name)

        if embed is not None:
            await logging_channel.send(embed=embed)
        
    async def on_member_ban(self, guild: discord.Guild, user: discord.User):
        logging_channel = get_logging_channel(guild, LOG_CHANNEL_NAME)
        
        title = "Member banned from server"
        description = f"**{user.name}** was banned from the server"
        embed = embed_builder(title, description, RED, user=user)
        await logging_channel.send(embed=embed)
    
    async def on_member_unban(self, guild: discord.Guild, user: discord.User):
        logging_channel = get_logging_channel(guild, LOG_CHANNEL_NAME)
        
        title = "Member unbanned from server"
        description = f"**{user.name}** was unbanned from the server"
        embed = embed_builder(title, description, GREEN, user=user)
        await logging_channel.send(embed=embed)


    async def on_member_join(self, member: discord.Member):
        logging_channel = get_logging_channel(member.guild, LOG_CHANNEL_NAME)

        title = "Member joined server"
        description = f"**{member.name}** joined the server"
        embed = embed_builder(title, description, GREEN, member=member)
        await logging_channel.send(embed=embed)


    async def on_member_remove(self, member: discord.Member):
        logging_channel = get_logging_channel(member.guild, LOG_CHANNEL_NAME)

        title = "Member left server"
        description = f"**{member.name}** left the server"
        embed = embed_builder(title, description, RED, member=member)
        await logging_channel.send(embed=embed)



load_dotenv()
TOKEN = os.getenv("MAIN")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.moderation = True
intents.voice_states = True
client = CustomBot(intents=intents)
client.run(TOKEN)