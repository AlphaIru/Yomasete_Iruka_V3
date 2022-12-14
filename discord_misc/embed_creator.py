"""Embedとかのコード."""
# coding: utf-8

import discord


bot_id_to_color = {
    813401103270019102: 0xFF8000,
    820128974176649266: 0xF5B0D6,
}


async def create_embed(ctx, bot_id, r_msg, ext_data=None):
    """Embedを作成."""
    bot_color = bot_id_to_color[bot_id]
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

    if ext_data is None:
        for addon_index, addon_items in r_msg["em_addons"].items():
            embed.add_field(
                name=addon_index,
                value=addon_items,
                inline=False,
            )
    else:
        for addon_index, addon_items in r_msg["em_addons"].items():
            embed.add_field(
                name=addon_items,
                value=ext_data[addon_index],
                inline=False,
            )

    if hasattr(ctx, "respond"):
        await ctx.respond(embed=embed)
    else:
        await ctx.send(embed=embed)
    return
