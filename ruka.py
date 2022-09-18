"""ルカのメインコード."""
# coding: utf-8

import time
import traceback

import discord
from discord import ApplicationContext
from discord.commands import SlashCommandGroup
from discord.ext import commands

from discord_misc.embed_creator import create_embed

from semi_secret.log import make_new_log
from semi_secret.get_token import get_token
from messages.get_message import get_pronoun, get_message
from messages.slash import get_slash_messages


BOT_COLOR = 0xF5B0D6
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


class MiscCommands(commands.Cog, name="Miscellaneous"):
    """ヘルプとかのコマンドを保存してる場所."""

    def __init__(self, bot: discord.Bot):
        """MiscCommandsのイニシャライズ."""
        self.bot = bot

    miscellaneous = SlashCommandGroup(
        name="miscellaneous",
        description="Various tool like commands!",
    )

    @miscellaneous.command(
        name="ping",
        description=get_slash_messages("ping", "main", BOT_NAME, get_pronoun(BOT_NAME)),
    )
    async def ping(self, ctx: ApplicationContext):
        """BotへのLatency&処理時間 (通称: Ping) の計測."""
        if ctx.author.bot:
            return
        before = time.perf_counter()
        pong_latency = round(bot_client.latency * 1000, 2)
        pong_process = round((time.perf_counter() - before) * 1000, 2)
        message_lang = "Jp"
        r_msg, _ = await get_message(
            message_lang, BOT_CLIENT_ID, "ping", pong_latency, pong_process
        )
        await create_embed(ctx, BOT_COLOR, r_msg)
        return


try:
    bot_client.add_cog(MiscCommands(bot_client))
except Exception:  # pylint: disable=broad-except
    make_new_log(traceback.format_exc())

bot_client.run(get_token(BOT_NAME))
