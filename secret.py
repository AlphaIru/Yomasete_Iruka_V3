# coding: utf-8
"""Secret系のコード."""

import discord

from discord.ext import commands
from discord.ext.commands import cooldown
from discord.ext.commands.cooldowns import BucketType


from messages.get_message import get_message  # pylint: disable=import-error
from discord_misc.embed_creator import create_embed  # pylint: disable=import-error


# for debug:
message_lang = "En"


class SecretCommands(commands.Cog, name="Secret"):
    """コナミコードみたいな秘密のコマンドを保存してる場所."""

    def __init__(self, bot: discord.Bot):
        """SecretCommandsのイニシャライズ."""
        self.bot = bot

    @commands.command(
        name="credit",
        aliases=[
            "credits",
            "staff",
            "staffs",
            "staffcredits",
            "staffcredit",
            "author",
            "authors",
        ]
    )
    @cooldown(1, 150, BucketType.user)
    async def credit(self, ctx):
        """クレジットの表示."""
        if ctx.author.bot:
            return
        r_msg, _ = await get_message(message_lang, self.bot.user.id, "credit")
        await ctx.channel.send(file=discord.File("/home/ubuntu/Yomasete_Iruka.jpeg"))
        await create_embed(ctx, self.bot.user.id, r_msg)
        return


def setup(bot):
    """このclassを追加."""
    bot.add_cog(SecretCommands(bot))


def teardown(bot):
    """このclassを排除."""
    bot.remove_cog(SecretCommands(bot))
