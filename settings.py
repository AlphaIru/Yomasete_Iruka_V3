# coding: utf-8
"""設定系のコード."""

# import uuid
# import time
import discord

from discord.ext import commands


# for debug:
MESSAGE_LANG = "En"


class SettingsCommands(commands.Cog, name="Settings"):
    """設定とかのコマンドを保存してる所."""

    def __init__(self, bot: discord.Bot):
        """SettingCommandsのイニシャライズ."""
        self.bot = bot


def setup(bot):
    """このclassを追加."""
    bot.add_cog(SettingsCommands(bot))


def teardown(bot):
    """このclassを排除."""
    bot.remove_cog(SettingsCommands(bot))
