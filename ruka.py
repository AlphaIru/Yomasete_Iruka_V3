"""ルカのメインコード."""
# coding: utf-8

import traceback

import discord
from discord import ApplicationContext, DiscordException, ExtensionNotLoaded, ExtensionAlreadyLoaded
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord.ext.commands import NotOwner, CommandOnCooldown

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
bot_client = discord.AutoShardedBot(
    command_prefix=PREFIX,
    intents=intents,
    owner_id=425848318044930048,
)

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
    for cog_file in cogs_list:
        bot_client.load_extension(f"{cog_file}")
except Exception:  # pylint: disable=broad-except
    make_new_log(traceback.format_exc())


class Debug(commands.Cog):
    """デバッグコマンド."""

    def __init__(self, bot_: discord.Bot):
        """init."""
        self.bot = bot_

    debug = SlashCommandGroup(
        name="debug",
        description="Debug Commands",
        checks=[commands.is_owner().predicate],
    )

    @debug.command(
        name="load",
        description="Loads extensions",
    )
    async def load(self, ctx: ApplicationContext):
        """デバッグコマンド: Load."""
        await ctx.respond("Loading extensions...")
        try:
            for cog in cogs_list:
                bot_client.load_extension(f"{cog}")
            await ctx.send("Successfully loaded extensions!")
        except ExtensionAlreadyLoaded:
            await ctx.send("Extension Already Loaded!")
        except Exception:  # pylint: disable=broad-except
            make_new_log(traceback.format_exc())
            await ctx.send("Failed loading extensions!")
        return

    @debug.command(
        name="unload",
        description="Unloads extensions",
    )
    async def unload(self, ctx: ApplicationContext):
        """デバッグコマンド: Unload."""
        await ctx.respond("Unloading extensions...")
        try:
            for cog in cogs_list:
                bot_client.unload_extension(f"{cog}")
            await ctx.send("Successfully unloaded extensions!")
        except ExtensionNotLoaded:
            await ctx.send("Extension Not Loaded!")
        except Exception:  # pylint: disable=broad-except
            make_new_log(traceback.format_exc())
            await ctx.send("Failed unloading extensions!")
        return

    @debug.command(
        name="reload",
        description="Unloads extensions",
    )
    async def reload(self, ctx: ApplicationContext):
        """デバッグコマンド: Reload."""
        await ctx.respond("Reloading extensions...")
        try:
            for cog in cogs_list:
                bot_client.reload_extension(f"{cog}")
            await ctx.send("Successfully reloaded extensions!")
        except ExtensionNotLoaded:
            await ctx.send("Extension Not Loaded!")
        except ExtensionAlreadyLoaded:
            await ctx.send("Extension Already Loaded!")
        except Exception:  # pylint: disable=broad-except
            make_new_log(traceback.format_exc())
            await ctx.send("Failed reloading extensions!")
        return

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: ApplicationContext, error: DiscordException):
        """コマンドエラーの対処."""
        if isinstance(error, CommandOnCooldown):
            await ctx.respond("Currently in maintenance, please refrain from using this bot.")
        elif isinstance(error, NotOwner):
            await ctx.respond("I don't know how you got here, but you can't use that command!")
        else:
            raise error  # Raise other errors so they aren't ignored
        return


bot_client.add_cog(Debug(bot_client))
bot_client.run(get_token(BOT_NAME))
