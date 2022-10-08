# coding: utf-8
"""設定系のコード."""

# import uuid
# import time
import discord

from discord import ApplicationContext
from discord.commands import option, SlashCommandGroup
from discord.ext import commands
from discord.ext.commands import guild_only, cooldown
from discord.ext.commands.cooldowns import BucketType


from messages.slash import slash_messages  # pylint: disable=import-error
from messages.get_message import get_message  # pylint: disable=import-error
from discord_misc.embed_creator import create_embed  # pylint: disable=import-error


# for debug:
MESSAGE_LANG = "En"


class SettingsCommands(commands.Cog, name="Settings"):
    """設定とかのコマンドを保存してる所."""

    def __init__(self, bot: discord.Bot):
        """SettingCommandsのイニシャライズ."""
        self.bot = bot

    settings = SlashCommandGroup(
        name="settings",
        description="Commands to manipulate settings!",
    )

    @settings.command(
        name="name",
        description=slash_messages["name"]["main"],
    )
    @option(
        name="read_name",
        description=slash_messages["name"]["read_name"],
    )
    @guild_only()
    @cooldown(2, 60, BucketType.user)
    async def name(
        self,
        ctx: ApplicationContext,
        read_name: bool,
    ):
        """メッセージの作者を読み上げるかどうかの設定."""
        await ctx.send("Done!")


def setup(bot):
    """このclassを追加."""
    bot.add_cog(SettingsCommands(bot))


def teardown(bot):
    """このclassを排除."""
    bot.remove_cog(SettingsCommands(bot))
