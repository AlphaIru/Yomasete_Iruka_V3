"""Embedとかのコード."""
# coding: utf-8

import discord


async def create_embed(
    ctx,
    bot_color,
    r_msg,
):
    """Embedを作成."""
    if "url" in r_msg:
        embed = discord.Embed(
            title=r_msg["title"],
            url=r_msg["url"],
            description=r_msg["description"],
            color=(bot_color),
        )
    else:
        embed = discord.Embed(
            title=r_msg["title"],
            description=r_msg["description"],
            color=(bot_color),
        )
    if "em_addons" not in r_msg:
        await ctx.respond(embed=embed)
        return

    for addon_index, addon_items in r_msg["em_addons"].items():
        embed.add_field(
            name=addon_index,
            value=addon_items,
            inline=False,
        )

    await ctx.respond(embed=embed)
    return