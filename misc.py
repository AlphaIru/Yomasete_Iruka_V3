# coding: utf-8
"""Help系のコード."""

import time
import discord
from discord import ApplicationContext
from discord.commands import SlashCommandGroup
from discord.ext import commands
from discord.ext.commands import cooldown
from discord.ext.commands.cooldowns import BucketType


from messages.slash import slash_messages  # pylint: disable=import-error
from messages.get_message import get_message  # pylint: disable=import-error
from discord_misc.embed_creator import create_embed  # pylint: disable=import-error

# for debug:
MESSAGE_LANG = "En"


class MiscCommands(commands.Cog, name="Miscellaneous"):
    """ヘルプとかのコマンドを保存してる場所."""

    def __init__(self, bot: discord.Bot):
        """MiscCommandsのイニシャライズ."""
        self.bot = bot

    miscellaneous = SlashCommandGroup(
        name="miscellaneous",
        description="Various tool like commands!",
    )

    documentations = miscellaneous.create_subgroup(
        name="documentations",
        description="Links to the documentations of this bot!",
    )

    @miscellaneous.command(
        name="bot_discord_links",
        description=slash_messages["botdiscordlink"]["main"],
    )
    @cooldown(2, 60, BucketType.user)
    async def bot_link(self, ctx: ApplicationContext):
        """イルカのリンクを送るコマンド."""
        if ctx.author.bot:
            return
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, "botdiscordlink")
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @documentations.command(
        name="help",
        description=slash_messages["help"]["main"],
    )
    @cooldown(2, 60, BucketType.user)
    async def help(self, ctx: discord.ApplicationContext):
        """ヘルプサイトのリンクを表示."""
        if ctx.author.bot:
            return
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, "help")
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @miscellaneous.command(
        name="ping",
        description=slash_messages["ping"]["main"],
    )
    @cooldown(2, 60, BucketType.user)
    async def ping(self, ctx: ApplicationContext):
        """BotへのLatency&処理時間 (通称: Ping) の計測."""
        if ctx.author.bot:
            return
        before = time.perf_counter()
        pong_latency = round(self.bot.latency * 1000, 2)
        pong_process = round((time.perf_counter() - before) * 1000, 2)
        r_msg, _ = await get_message(
            MESSAGE_LANG, self.bot.user.id, "ping", pong_latency, pong_process
        )
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @documentations.command(
        name="troubleshoot", description=slash_messages["troubleshoot"]["main"]
    )
    @cooldown(2, 60, BucketType.user)
    async def troubleshoot(self, ctx: ApplicationContext):
        """トラブルシュートの表示."""
        if ctx.author.bot:
            return
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, "troubleshoot")
        await create_embed(ctx, self.bot.user.id, r_msg)
        return

    @documentations.command(
        description=slash_messages["voicelist"]["main"],
    )
    @cooldown(2, 60, BucketType.user)
    async def voicelist(self, ctx: ApplicationContext):
        """使えるボイスリストの表示."""
        if ctx.author.bot:
            return
        r_msg, _ = await get_message(MESSAGE_LANG, self.bot.user.id, "voicelist")
        await create_embed(ctx, self.bot.user.id, r_msg)
        return


def setup(bot):
    """このclassを追加."""
    bot.add_cog(MiscCommands(bot))


def teardown(bot):
    """このclassを排除."""
    bot.remove_cog(MiscCommands(bot))
