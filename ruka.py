# coding: utf-8
"""ルカのメインコード."""

import traceback

import discord
from discord import (
    ApplicationContext,
    DiscordException,
    ExtensionAlreadyLoaded,
    ExtensionNotFound,
    ExtensionNotLoaded,
)
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown, NotOwner

from discord_misc.embed_creator import create_embed  # pylint: disable=import-error
from messages.get_message import get_message  # pylint: disable=import-error
from semi_secret.get_token import get_token  # pylint: disable=import-error
from semi_secret.log import make_new_log  # pylint: disable=import-error

# for debug:
MESSAGE_LANG = "En"


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
bot_client = commands.AutoShardedBot(
    command_prefix=PREFIX,
    intents=intents,
    owner_id=425848318044930048,
)

cogs_list = ["misc", "secret"]


class GuildData: # pylint: disable=too-few-public-methods
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
    for cog_file in cogs_list:
        bot_client.load_extension(f"{cog_file}")
except Exception:  # pylint: disable=broad-except
    make_new_log(traceback.format_exc())


class DebugCommands(commands.Cog):
    """デバッグコマンド."""

    def __init__(self, bot_: discord.Bot):
        """init."""
        self.bot = bot_

    @commands.group()
    async def debug(self, ctx: ApplicationContext):  # pylint: disable=unused-argument
        """debugのgroup."""
        return

    @debug.command(
        name="load",
        description="Loads extensions",
        checks=[commands.is_owner().predicate],
    )
    async def load(self, ctx: ApplicationContext, cogname=None):
        """デバッグコマンド: Load."""
        await ctx.message.delete()
        if cogname:
            await ctx.send(f"Loading {cogname}", delete_after=10)
            try:
                bot_client.load_extension(f"{cogname}")
                await ctx.send(f"Successfully loaded {cogname}!", delete_after=10)
            except ExtensionNotFound:
                await ctx.send(f"{cogname} is not Found!", delete_after=10)
            except ExtensionAlreadyLoaded:
                await ctx.send(f"{cogname} is already loaded!", delete_after=10)
            except Exception:  # pylint: disable=broad-except
                make_new_log(traceback.format_exc())
                await ctx.send(f"Failed loading {cogname}!", delete_after=10)
            return
        await ctx.send("Loading extensions...", delete_after=10)
        try:
            for cog in cogs_list:
                bot_client.load_extension(f"{cog}")
            await ctx.send("Successfully loaded extensions!", delete_after=10)
        except ExtensionNotFound:
            await ctx.send("Extension Not Found!", delete_after=10)
        except ExtensionAlreadyLoaded:
            await ctx.send("Extension Already Loaded!", delete_after=10)
        except Exception:  # pylint: disable=broad-except
            make_new_log(traceback.format_exc())
            await ctx.send("Failed loading extensions!", delete_after=10)
        return

    @debug.command(
        name="unload",
        description="Unloads extensions",
        checks=[commands.is_owner().predicate],
    )
    async def unload(self, ctx: ApplicationContext, cogname=None):
        """デバッグコマンド: Unload."""
        await ctx.message.delete()
        if cogname:
            await ctx.send(f"Unloading {cogname}", delete_after=10)
            try:
                bot_client.unload_extension(f"{cogname}")
                await ctx.send(f"Successfully unloaded {cogname}!", delete_after=10)
            except ExtensionNotLoaded:
                await ctx.send(f"{cogname} is not loaded!", delete_after=10)
            except Exception:  # pylint: disable=broad-except
                make_new_log(traceback.format_exc())
                await ctx.send(f"Failed unloading {cogname}!", delete_after=10)
            return
        await ctx.send("Unloading extensions...", delete_after=10)
        try:
            for cog in cogs_list:
                bot_client.unload_extension(f"{cog}")
            await ctx.send("Successfully unloaded extensions!", delete_after=10)
        except ExtensionNotLoaded:
            await ctx.send("Extension Not Loaded!", delete_after=10)
        except Exception:  # pylint: disable=broad-except
            make_new_log(traceback.format_exc())
            await ctx.send("Failed unloading extensions!", delete_after=10)
        return

    @debug.command(
        name="reload",
        description="Unloads extensions",
        checks=[commands.is_owner().predicate],
    )
    # pylama: ignore=C901
    async def reload(self, ctx: ApplicationContext, cogname=None):
        """デバッグコマンド: Reload."""
        await ctx.message.delete()
        if cogname:
            await ctx.send(f"Reloading {cogname}", delete_after=10)
            try:
                bot_client.reload_extension(f"{cogname}")
                await ctx.send(f"Successfully reloaded {cogname}!", delete_after=10)
            except ExtensionAlreadyLoaded:
                await ctx.send(f"{cogname} is already loaded!", delete_after=10)
            except ExtensionNotLoaded:
                await ctx.send(f"{cogname} is not loaded!", delete_after=10)
            except Exception:  # pylint: disable=broad-except
                make_new_log(traceback.format_exc())
                await ctx.send(f"Failed reloading {cogname}!", delete_after=10)
            return
        await ctx.send("Reloading extensions...", delete_after=10)
        try:
            for cog in cogs_list:
                bot_client.reload_extension(f"{cog}")
            await ctx.send("Successfully reloaded extensions!", delete_after=10)
        except ExtensionNotLoaded:
            await ctx.send("Extension Not Loaded!", delete_after=10)
        except ExtensionAlreadyLoaded:
            await ctx.send("Extension Already Loaded!", delete_after=10)
        except Exception:  # pylint: disable=broad-except
            make_new_log(traceback.format_exc())
            await ctx.send("Failed reloading extensions!", delete_after=10)
        return


@bot_client.event
async def on_command_error(ctx: ApplicationContext, error: DiscordException):
    """エラーが発生したときのコマンド."""
    if isinstance(error, CommandOnCooldown):
        r_msg, _ = await get_message(
            MESSAGE_LANG, bot_client.user.id, "cooldown", int(error.retry_after)
        )
        await create_embed(ctx, bot_client.user.id, r_msg)
    elif isinstance(error, NotOwner):
        await ctx.send(
            "I don't know how you got here, but you can't use that command!",
            delete_after=10,
        )
        return
    return


@bot_client.event
async def on_application_command_error(
    ctx: ApplicationContext, error: DiscordException
):
    """コマンドエラーの対処."""
    if isinstance(error, CommandOnCooldown):
        r_msg, _ = await get_message(
            MESSAGE_LANG, bot_client.user.id, "cooldown", int(error.retry_after)
        )
    elif isinstance(error, NotOwner):
        await ctx.send(
            "I don't know how you got here, but you can't use that command!",
            delete_after=10,
        )
        return
    else:
        r_msg, _ = await get_message(
            MESSAGE_LANG, bot_client.user.id, "unknownerror", error
        )
        await create_embed(ctx, bot_client.user.id, r_msg)
        make_new_log(error)
        raise error
    await create_embed(ctx, bot_client.user.id, r_msg)
    return


bot_client.add_cog(DebugCommands(bot_client))
bot_client.run(get_token(BOT_NAME))
