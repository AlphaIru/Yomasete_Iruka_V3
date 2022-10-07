# coding: utf-8
"""メッセージを返信するための関数."""


from .japanese_message import get_jp_msg_voice
from .english_message import get_en_msg_voice


id_to_name = {
    813401103270019102: {
        "Jp": "イルーくん",
        "En": "Iru",
    },
    820128974176649266: {
        "Jp": "ルカちゃん",
        "En": "Ruka",
    },
    906641565441736744: {
        "Jp": "ドルンたん",
        "En": "Dolun",
    },
    906641635092332586: {
        "Jp": "フィンタくん",
        "En": "Finta",
    },
    906643085264572426: {
        "Jp": "セテさん",
        "En": "Cete",
    },
}

list_type_to_name = {
    False: {
        "Jp": "ブラックリスト",
        "En": "Blacklist",
    },
    True: {
        "Jp": "ホワイトリスト",
        "En": "Whitelist",
    },
}


async def get_text_message(
    bot_id, bot_name, message_type, lang, input1="", input2=""
):
    """テキストメッセージを返す関数."""
    if lang == "Jp":
        return await get_jp_msg_voice(bot_name, bot_id, message_type, input1, input2)
    elif lang == "En":
        return await get_en_msg_voice(bot_name, bot_id, message_type, input1, input2)


async def get_message(
    lang="Jp", bot_id=813401103270019102, message_type="help", input1="", input2=""
):
    """メッセージを返す関数."""
    try:
        bot_name = id_to_name[bot_id][lang]  # noqa: F841
    except KeyError:
        bot_name = "Iru"

    text_message, voice_message = await get_text_message(
        bot_id, bot_name, message_type, lang, input1, input2
    )
    return (text_message, voice_message)


async def get_bored_message(lang="Jp"):
    """お遊びメッセージを返す関数."""
    if lang == "En":
        return "I'm bored, can I talk?"
    return "暇だよー、何か話していい?"


async def get_callout_message(callout_type="None", lang="Jp", display_name=""):
    """コールアウトメッセージを返す関数."""
    callout_message = {
        "None": {
            "Jp": "なし",
            "En": "None",
        },
        "VoiceChat_In": {
            "Jp": f"{display_name}がボイチャに入ったよー!",
            "En": f"{display_name} has joined in the voice channel!",
        },
        "VoiceChat_Out": {
            "Jp": f"{display_name}がボイチャから出たよー!",
            "En": f"{display_name} has left the voice channel!",
        },
        "VoiceChat_In_From_Out": {
            "Jp": f"{display_name}が他のボイチャから入ったよー!",
            "En": (
                f"{display_name} has joined in the voice channel from the different voice channel!"
            ),
        },
        "VoiceChat_Out_From_In": {
            "Jp": f"{display_name}が他のボイチャに行ったよー!",
            "En": f"{display_name} has left the voice channel to the different voice channel!",
        },
        "Server_Deaf_On": {
            "Jp": f"{display_name}がサーバー側のスピーカーミュートされたよ!",
            "En": f"{display_name} has been server deafened!",
        },
        "Server_Deaf_Off": {
            "Jp": f"{display_name}がサーバー側のスピーカーミュートが外されたよ!",
            "En": f"{display_name} is not server deafened anymore!",
        },
        "Server_Mute_On": {
            "Jp": f"{display_name}がサーバー側のミュートされたよ!",
            "En": f"{display_name} has been deafened!",
        },
        "Server_Mute_Off": {
            "Jp": f"{display_name}がサーバー側のミュートが外されたよ!",
            "En": f"{display_name} is not deafened anymore!",
        },
        "Self_Deaf_On": {
            "Jp": f"{display_name}がスピーカーミュートをつけたよ!",
            "En": f"{display_name} is deafened!",
        },
        "Self_Deaf_Off": {
            "Jp": f"{display_name}がスピーカーミュートを外したよ!",
            "En": f"{display_name} is not deafened anymore!",
        },
        "Self_Mute_On": {
            "Jp": f"{display_name}がミュートをつけたよ!",
            "En": f"{display_name} is muted!",
        },
        "Self_Mute_Off": {
            "Jp": f"{display_name}がミュートを外したよ!",
            "En": f"{display_name} is not muted anymore!",
        },
        "Self_Stream_On": {
            "Jp": f"{display_name}が画面配信を始めたよ!",
            "En": f"{display_name} has started streaming!",
        },
        "Self_Stream_Off": {
            "Jp": f"{display_name}が画面配信を止めたよ!",
            "En": f"{display_name} has stopped streaming!",
        },
        "Self_Video_On": {
            "Jp": f"{display_name}がウェブカメラをつけたよ!",
            "En": f"{display_name} has turned on the web camera!",
        },
        "Self_Video_Off": {
            "Jp": f"{display_name}がウェブカメラを止めたよ!",
            "En": f"{display_name} has turned off the web camera!",
        },
    }
    return callout_message[callout_type][lang]


def get_pronoun(bot_client):
    """代名詞を取得する."""
    if bot_client == 820128974176649266:
        return "her"
    return "his"
