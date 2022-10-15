# coding: utf-8
"""データベースの作成."""
import asyncio
import sqlite3
from sqlite3 import Error


async def sql_guild_connect():
    """guild.dbへの接続."""
    try:
        return sqlite3.connect("./Yomasete_Iruka_V3/database/guild/guild.db")
    except Error:
        print(Error)


async def create_table():
    """メインコード."""
    guild_con = await sql_guild_connect()
    guild_cursor = guild_con.cursor()

    while True:
        create_guild_table = "CREATE TABLE IF NOT EXISTS settings \
            (id INTEGER PRIMARY KEY, read_name INTEGER, read_bot INTEGER, read_mention INTEGER, \
            read_other_bot INTEGER);"
        guild_cursor.execute(create_guild_table)

        if len(guild_cursor.execute("SELECT * FROM settings;").description) == 5:
            break
        else:
            guild_con.close()
            await delete_table()
            guild_con = await sql_guild_connect()
            guild_cursor = guild_con.cursor()

    guild_con.commit()
    guild_con.close()


async def delete_table():
    """デバック系のコード."""
    guild_con = await sql_guild_connect()
    guild_cursor = guild_con.cursor()

    guild_cursor.execute("DROP TABLE IF EXISTS settings;")

    guild_con.commit()
    guild_con.close()


if __name__ == "__main__":
    asyncio.run(delete_table())
    asyncio.run(create_table())
