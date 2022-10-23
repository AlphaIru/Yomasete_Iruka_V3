# coding: utf-8
"""設定系のコード."""

# import uuid
# import time
# import asyncio

import discord
from discord import ApplicationContext
from discord.commands import option, SlashCommandGroup
from discord.ext import commands
from discord.ext.commands import guild_only, cooldown, has_permissions
from discord.ext.commands.cooldowns import BucketType

from messages.slash import slash_messages  # pylint: disable=import-error
from messages.get_message import get_message  # pylint: disable=import-error
from discord_misc.embed_creator import create_embed  # pylint: disable=import-error
from discord_misc.database_editor import commit_guild_settings  # pylint: disable=import-error
from discord_misc.database_editor import commit_userjoin_settings  # pylint: disable=import-error


# for debug:
MESSAGE_LANG = "En"

bot_lang_choices = {
    "En": 0,
    "Jp": 1,
}


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

    preference = settings.create_subgroup(
        name="preference",
        description="Settings related to bots' actions on messages and commands.",
    )

    @read_out.command(
        name="emoji",
        description=slash_messages["emoji"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["emoji"]["read_emoji"],
    )
    @cooldown(2, 60, BucketType.user)
    @guild_only()
    @has_permissions(administrator=True)
    async def emoji(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
    ):
        """絵文字の読み上げの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("read_emoji", ctx.guild.id, boolean)
        msg_name = "reademoji_T" if boolean else "reademoji_F"
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
    @has_permissions(administrator=True)
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
        name="name",
        description=slash_messages["name"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["name"]["read_name"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
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
    @has_permissions(administrator=True)
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
        name="other_bots_messages",
        description=slash_messages["readotherbot"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["readotherbot"]["read_other_bot"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
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

    @read_out.command(
        name="non_vc_users_message",
        description=slash_messages["readotherusers"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["readotherusers"]["read_non_vc_users_message"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
    async def readotherusers(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
    ):
        """ボイチャ以外のユーザーの文章の読み上げ."""
        if ctx.author.bot:
            return
        await commit_guild_settings("read_outside_user", ctx.guild.id, boolean)
        msg_name = "readoutsideusers_T" if boolean else "readoutsideusers_F"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name)
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @read_out.command(
        name="voicechat_actions",
        description=slash_messages["userjoin"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["userjoin"]["user_join"],
    )
    @option(
        name="join_leave",
        description=slash_messages["userjoin"]["join_leave"],
    )
    @option(
        name="guild_deaf",
        description=slash_messages["userjoin"]["guild_deaf"],
    )
    @option(name="guild_mute", description=slash_messages["userjoin"]["guild_mute"])
    @option(
        name="self_deaf",
        description=slash_messages["userjoin"]["self_deaf"],
    )
    @option(
        name="self_mute",
        description=slash_messages["userjoin"]["self_mute"],
    )
    @option(
        name="self_stream",
        description=slash_messages["userjoin"]["self_stream"],
    )
    @option(name="self_video", description=slash_messages["userjoin"]["self_video"])
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
    async def userjoin(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
        join_leave: bool,
        guild_deaf: bool,
        guild_mute: bool,
        self_deaf: bool,
        self_mute: bool,
        self_stream: bool,
        self_video: bool,
    ):
        """ボイチャでのユーザー操作の読み上げ."""
        if ctx.author.bot:
            return
        if boolean:
            userjoin_settings = {
                0: join_leave,
                1: guild_deaf,
                2: guild_mute,
                3: self_deaf,
                4: self_mute,
                5: self_stream,
                6: self_video,
            }
            await commit_userjoin_settings(ctx.guild.id, userjoin_settings)
            msg_name = "userjoin_T"
        else:
            userjoin_settings = None
            msg_name = "userjoin_F"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name, userjoin_settings)
        await create_embed(ctx, self.bot.user.id, r_msg, userjoin_settings)
        return

    @preference.command(
        name="auto_delete_bot_messages",
        description=slash_messages["deletebotmessages"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["deletebotmessages"]["delete_bot_messages"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
    async def deletebotmessages(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
    ):
        """一定時間後、Bot文の削除の設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("delete_bot_messages", ctx.guild.id, boolean)
        msg_name = "deletebotmessage_T" if boolean else "deletebotmessage_F"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name)
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @preference.command(
        name="force_japanese_voice",
        description=slash_messages["forcejapanese"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["forcejapanese"]["force_japanese_mode"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
    async def forcejapanese(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
    ):
        """ユーザーの文章を強制的に日本語で読み上げの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("force_japanese_voice", ctx.guild.id, boolean)
        msg_name = "forcejapanese_T" if boolean else "forcejapanese_F"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name)
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @preference.command(
        name="change_language",
        description=slash_messages["language"]["main"],
    )
    @option(
        name="select_language",
        description=slash_messages["language"]["lang"],
        choices=bot_lang_choices,
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
    async def language(
        self,
        ctx: discord.ApplicationContext,
        select_language: str,
    ):
        """Bot言語の設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings(
            "language", ctx.guild.id, bot_lang_choices[select_language]
        )
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, "language")
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @preference.command(
        name="word_limit",
        description=slash_messages["length"]["main"],
    )
    @option(
        name="limit",
        description=slash_messages["length"]["limit"],
        min_value=200,
        max_value=2000,
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
    async def length(
        self,
        ctx: discord.ApplicationContext,
        limit: int,
    ):
        """文章読み上げの長さの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("length", ctx.guild.id, limit)
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, "word_limit")
        await create_embed(ctx, self.bot.user.id, r_msg, limit)
        return

    @preference.command(
        name="toggle_whitelist_mode",
        description=slash_messages["switchblacklist"]["main"],
    )
    @option(
        name="boolean",
        description=slash_messages["switchblacklist"]["switch_blacklist"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
    async def switchblacklist(
        self,
        ctx: discord.ApplicationContext,
        boolean: bool,
    ):
        """ブラックリスト・ホワイトリストの切り替えの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("whitelist", ctx.guild.id, boolean)
        msg_name = "whitelist" if boolean else "blacklist"
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, msg_name)
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @preference.command(
        name="afk_timeout",
        description=slash_messages["afktimeout"]["main"],
    )
    @option(
        name="limit",
        description=slash_messages["afktimeout"]["limit"],
        min_value=0,
        max_value=6000,
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    @has_permissions(administrator=True)
    async def afk_timeout(
        self,
        ctx: discord.ApplicationContext,
        limit: int,
    ):
        """イルカが自動で抜ける時間の長さの設定."""
        if ctx.author.bot:
            return
        await commit_guild_settings("afk_timeout", ctx.guild.id, limit)
        if limit > 0:
            limit_minute = limit // 60
            limit_second = limit % 60
            r_msg, _ = await get_message(
                MESSAGE_LANG,
                self.bot.user.id,
                "afktimeout_T",
                limit_minute,
                limit_second,
            )
        else:
            r_msg, _ = await get_message(
                MESSAGE_LANG,
                self.bot.user.id,
                "afktimeout_F",
                limit_minute,
                limit_second,
            )
        await create_embed(ctx, self.bot.user.id, r_msg, limit)
        return


def setup(bot):
    """このclassを追加."""
    bot.add_cog(SettingsCommands(bot))
    return


def teardown(bot):
    """このclassを排除."""
    bot.remove_cog(SettingsCommands(bot))
    return
