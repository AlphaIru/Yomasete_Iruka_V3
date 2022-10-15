# coding: utf-8
"""設定系のコード."""

# import uuid
# import time
# import asyncio
import sqlite3
from sqlite3 import Error

import discord
from discord import ApplicationContext
from discord.commands import option, SlashCommandGroup
from discord.ext import commands
from discord.ext.commands import guild_only, cooldown
from discord.ext.commands.cooldowns import BucketType


from messages.slash import slash_messages  # pylint: disable=import-error
from messages.get_message import get_message  # pylint: disable=import-error
from semi_secret.log import make_new_log  # pylint: disable=import-error
from discord_misc.embed_creator import create_embed  # pylint: disable=import-error


# for debug:
MESSAGE_LANG = "En"


async def commit_guild_settings(setting_name: str, guild_id: int, selected_bool: bool):
    """ギルドの設定の変更を実行する."""
    try:
        guild_con = sqlite3.connect("./Yomasete_Iruka_V3/database/guild/guild.db")
    except Error as e_msg:
        await make_new_log(e_msg)
        raise e_msg
    guild_cursor = guild_con.cursor()

    check_settings = "SELECT ? FROM settings WHERE id = ?;"
    guild_cursor.execute(
        check_settings,
        (
            setting_name,
            guild_id,
        ),
    )

    if not guild_cursor.fetchall():
        add_settings = "INSERT INTO settings VALUES (?, 0, 0, 0, 0);"
        guild_cursor.execute(add_settings, (guild_id,))

    # ↓ 入れてるのはこのファイルにハードコードされた「設定科目名」だからSQL Injectionの心配は一応なし。
    edit_settings = f"UPDATE settings SET {setting_name} = ? WHERE id = ?;"  # nosec
    guild_cursor.execute(
        edit_settings,
        (
            selected_bool,
            guild_id,
        ),
    )

    guild_con.commit()
    guild_con.close()


class SettingsCommands(commands.Cog, name="Settings"):
    """設定とかのコマンドを保存してる所."""

    def __init__(self, bot: discord.Bot):
        """SettingCommandsのイニシャライズ."""
        self.bot = bot
        return

    settings = SlashCommandGroup(
        name="settings",
        description="Commands to manipulate settings!",
    )

    read_out = settings.create_subgroup(
        name="read_out",
        description="Settings related to reading out messages.",
    )

    @read_out.command(
        name="name",
        description=slash_messages["name"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["name"]["read_name"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    async def name(
        self,
        ctx: ApplicationContext,
        boolean: bool,
    ):
        """メッセージの作者を読み上げるかどうかの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("read_name", ctx.guild.id, boolean)
        msg_name = "readname_T" if boolean else "readname_F"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name)
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @read_out.command(
        name="dolphin_messages",
        description=slash_messages["readbot"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["readbot"]["read_bot"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    async def readbot(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
    ):
        """メッセージの作者を読み上げるかどうかの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("read_bot", ctx.guild.id, boolean)
        msg_name = "readbot_T" if boolean else "readbot_F"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name)
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @read_out.command(
        name="mention",
        description=slash_messages["mention"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["mention"]["read_mention"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    async def mention(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
    ):
        """メンションの読み上げの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("read_mention", ctx.guild.id, boolean)
        msg_name = "mention_T" if boolean else "mention_F"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name)
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @read_out.command(
        name="other_bots_messages",
        description=slash_messages["readotherbot"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["readotherbot"]["read_other_bot"],
    )
    @cooldown(2, 60, BucketType.user)
    @guild_only()
    async def readotherbot(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
    ):
        """他のBot文章の読み上げの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("read_other_bot", ctx.guild.id, boolean)
        msg_name = "readotherbot_T" if boolean else "readotherbot_F"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name)
        await create_embed(ctx, self.bot.user.id, r_msg)
        return


def setup(bot):
    """このclassを追加."""
    bot.add_cog(SettingsCommands(bot))
    return


def teardown(bot):
    """このclassを排除."""
    bot.remove_cog(SettingsCommands(bot))
    return
