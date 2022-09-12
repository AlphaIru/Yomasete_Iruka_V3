"""イルーのメインコード."""
# coding: utf-8

import discord
from discord.ext import commands
from return_token import get_token

BOT_NAME = "Ruka"
PREFIX = "!ruka "


CLIENT_ID = 0
CLIENT_NAME = ""


class GuildData:
    """各アクティブなギルドのデータを一時保存する."""

    def __init__(self):
        """ギルドの設定."""


intents = discord.Intents(
    messages=True,
    message_content=True,
    guilds=True,
    members=True,
    voice_states=True,
    guild_reactions=True,
)
client = commands.AutoShardedBot(command_prefix=PREFIX, intents=intents)


async def set_client_id_name(client_data):
    """イルカの名前とIDを保存する."""
    global CLIENT_ID  # pylint: disable=global-statement
    global CLIENT_NAME  # pylint: disable=global-statement
    if CLIENT_ID == 0:
        CLIENT_ID = client_data.user.id
        print(CLIENT_ID)
    if CLIENT_NAME == "":
        CLIENT_NAME = client_data.user.name
        print(CLIENT_NAME)


@client.event
async def on_shard_connect(shard_id):
    """BotがDiscordに接続時にするコード."""
    print("------------------------------")
    print(f"#{shard_id} is connected")
    await set_client_id_name(client)
    print("------------------------------")


@client.event
async def on_shard_ready(shard_id):
    """BotがDiscordにログイン時にするコード."""
    print("------------------------------")
    print(f"#{shard_id} is logged in")
    await set_client_id_name(client)
    print("------------------------------")


@client.event
async def on_shard_disconnect(shard_id):
    """BotがDiscordから切断された時にするコード."""
    print("------------------------------")
    print(f"#{shard_id} is disconnected")
    await set_client_id_name(client)
    print("------------------------------")


@client.event
async def on_shard_resume(shard_id):
    """Discordに再接続した時のコード."""
    print("------------------------------")
    print(f"#{shard_id} resumed its connection to Discord")
    await set_client_id_name(client)
    print("------------------------------")


client.run(get_token(BOT_NAME))
