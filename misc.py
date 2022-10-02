"""Help系のコード."""
# coding: utf-8

import time

import discord
from discord import ApplicationContext
from discord.commands import SlashCommandGroup
from discord.ext import commands

from messages.slash import get_slash_messages  # pylint: disable=import-error
from messages.get_message import get_message  # pylint: disable=import-error
from discord_misc.embed_creator import create_embed  # pylint: disable=import-error

# for debug:
message_lang = "Jp"


class MiscCommands(commands.Cog, name="Miscellaneous"):
    """ヘルプとかのコマンドを保存してる場所."""

    def __init__(self, bot: discord.Bot):
        """MiscCommandsのイニシャライズ."""
        self.bot = bot

    @commands.Cog.listener(name="ready")
    async def on_ready(self):
        """Ready時のセットアップ."""
        return

    miscellaneous = SlashCommandGroup(
        name="miscellaneous",
        description="Various tool like commands!",
    )

    @miscellaneous.command(
        name="ping",
        description=get_slash_messages("ping", "main"),
    )
    async def ping(self, ctx: ApplicationContext):
        """BotへのLatency&処理時間 (通称: Ping) の計測."""
        if ctx.author.bot:
            return
        before = time.perf_counter()
        pong_latency = round(self.bot.latency * 1000, 2)
        pong_process = round((time.perf_counter() - before) * 1000, 2)
        r_msg, _ = await get_message(
            message_lang, self.bot.user.id, "ping", pong_latency, pong_process
        )
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @miscellaneous.command(
        name="bot_discord_links",
        description=get_slash_messages("botdiscordlink", "main"),
    )
    async def bot_link(self, ctx: ApplicationContext):
        """イルカのリンクを送るコマンド."""
        if ctx.author.bot:
            return
        r_msg, _ = await get_message(message_lang, self.bot.user.id, "botdiscordlink")
        await create_embed(ctx, self.bot.user.id, r_msg)
        return


def setup(bot):
    """このclassを追加."""
    bot.add_cog(MiscCommands(bot))
