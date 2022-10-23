"""guildの設定をデーターベースに反映するファイル."""
# coding: utf-8

import sqlite3
from sqlite3 import Error


async def commit_guild_settings(setting_name: str, guild_id: int, selected_bool: bool):
    """ギルドの設定の変更を実行する."""
    try:
        guild_con = sqlite3.connect("./Yomasete_Iruka_V3/database/guild/guild.db")
    except Error as e_msg:
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
        add_settings = "INSERT INTO settings VALUES (?, 0, 0, 0, 0, 0, 0);"
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


async def commit_userjoin_settings(guild_id: int, userjoin_settings: dict):
    """ギルドの設定の変更を実行する."""
    try:
        guild_con = sqlite3.connect("./Yomasete_Iruka_V3/database/guild/guild.db")
    except Error as e_msg:
        raise e_msg
    guild_cursor = guild_con.cursor()

    check_settings = "SELECT * FROM userjoin WHERE id = ?;"
    guild_cursor.execute(check_settings, (guild_id,))

    if not guild_cursor.fetchall():
        add_settings = "INSERT INTO userjoin VALUES (?, 1, 1, 1, 1, 1, 1, 1);"
        guild_cursor.execute(add_settings, (guild_id,))

    edit_settings = "UPDATE userjoin SET \
        join_leave = ?, \
        guild_deaf = ?, \
        guild_mute = ?, \
        self_deaf = ?, \
        self_mute = ?, \
        self_stream = ?, \
        self_video = ? \
        WHERE id = ?;"
    guild_cursor.execute(
        edit_settings,
        (
            userjoin_settings[0],
            userjoin_settings[1],
            userjoin_settings[2],
            userjoin_settings[3],
            userjoin_settings[4],
            userjoin_settings[5],
            userjoin_settings[6],
            guild_id,
        ),
    )

    guild_con.commit()
    guild_con.close()
