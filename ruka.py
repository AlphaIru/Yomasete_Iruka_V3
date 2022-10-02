"""ルカのメインコード."""
# coding: utf-8

import traceback

import discord
from discord.ext import commands

from semi_secret.log import make_new_log  # pylint: disable=import-error
from semi_secret.get_token import get_token  # pylint: disable=import-error


BOT_NAME = "Ruka"
PREFIX = "!ruka "

BOT_CLIENT_ID = 0
BOT_CLIENT_NAME = ""


intents = discord.Intents(
    messages=True,
    message_content=True,
    guilds=True,
    members=True,
    voice_states=True,
    guild_reactions=True,
)
bot_client = commands.AutoShardedBot(command_prefix=PREFIX, intents=intents)

cogs_list = ["misc"]


class GuildData:
    """各アクティブなギルドのデータを一時保存する."""

    def __init__(self):
        """ギルドの設定."""


async def set_bot_id_name(bot_data):
    """イルカの名前とIDを保存する."""
    global BOT_CLIENT_ID  # pylint: disable=global-statement
    global BOT_CLIENT_NAME  # pylint: disable=global-statement
    if BOT_CLIENT_ID == 0:
        BOT_CLIENT_ID = bot_data.user.id
        print(BOT_CLIENT_ID)
    if BOT_CLIENT_NAME == "":
        BOT_CLIENT_NAME = bot_data.user.name
        print(BOT_CLIENT_NAME)
    return


@bot_client.event
async def on_shard_connect(shard_id):
    """BotがDiscordに接続時にするコード."""
    print("------------------------------")
    print(f"#{shard_id} is connected")
    await set_bot_id_name(bot_client)
    print("------------------------------")
    return


@bot_client.event
async def on_shard_ready(shard_id):
    """BotがDiscordにログイン時にするコード."""
    print("------------------------------")
    print(f"#{shard_id} is logged in")
    await set_bot_id_name(bot_client)
    print("------------------------------")
    return


@bot_client.event
async def on_shard_disconnect(shard_id):
    """BotがDiscordから切断された時にするコード."""
    print("------------------------------")
    print(f"#{shard_id} is disconnected")
    await set_bot_id_name(bot_client)
    print("------------------------------")
    return


@bot_client.event
async def on_shard_resume(shard_id):
    """Discordに再接続した時のコード."""
    print("------------------------------")
    print(f"#{shard_id} resumed its connection to Discord")
    await set_bot_id_name(bot_client)
    print("------------------------------")
    return


try:
    for cog in cogs_list:
        bot_client.load_extension(f"{cog}")
except Exception:  # pylint: disable=broad-except
    make_new_log(traceback.format_exc())

bot_client.run(get_token(BOT_NAME))
