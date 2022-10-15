# coding: utf-8
"""ブラックリスト系のコード."""

import discord

from discord.ext import commands


class BlacklistCommands(commands.Cog, name="Blacklist"):
    """ブラックリストとかのコードを保存してる場所."""

    def __init__(self, bot: discord.Bot):
        """BlacklistCommandsのイニシャライズ."""
        self.bot = bot
        return


def setup(bot):
    """このclassを追加."""
    bot.add_cog(BlacklistCommands(bot))
    return


def teardown(bot):
    """このclassを排除."""
    bot.remove_cog(BlacklistCommands(bot))
    return
