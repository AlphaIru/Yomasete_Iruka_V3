"""日本語の文章などを取得."""
# coding: utf-8
# pylint: disable=line-too-long
# pylama: ignore=E501


jp_enumrated_voices = {
    0: "速度",
    1: "音程・音高",
    2: "アフリカーンス語",
    3: "アムハラ語",
    4: "アラゴン語",
    5: "アラビア語",
    6: "アッサム語",
    7: "アゼルバイジャン語",
    8: "バシキール語",
    9: "ブルガリア語",
    10: "ベンガル語",
    11: "ビシュヌプリヤ・マニプリ語",
    12: "ブルトン語",
    13: "ボスニア語",
    14: "カタロニア語",
    15: "チェコ語",
    16: "ウェールズ語",
    17: "デンマーク語",
    18: "ドイツ語",
    19: "ギリシャ語",
    20: "英語",
    21: "エスペラント語",
    22: "スペイン語",
    23: "エストニア語",
    24: "バスク語",
    25: "ペルシア語",
    26: "フィンランド語",
    27: "フランス語",
    28: "アイルランド・ゲール語",
    29: "スコットランド・ゲール語",
    30: "グアラニー語",
    31: "グジャラート語",
    32: "ヘブライ語",
    33: "ヒンディー語",
    34: "クロアチア語",
    35: "ハイチ・クレオール語",
    36: "ハンガリー語",
    37: "アルメニア語",
    38: "インターリングア",
    39: "インドネシア語",
    40: "アイスランド語",
    41: "イタリア語",
    42: "ロジバン語",
    43: "日本語",
    44: "ジョージア語",
    45: "カザフ語",
    46: "グリーンランド語",
    47: "カンナダ語",
    48: "韓国・ハングル語",
    49: "コンカニ語",
    50: "クルマンジー・クルド語",
    51: "キルギス語",
    52: "ラテン語",
    53: "リングア・フランカ・ノバ",
    54: "リトアニア語",
    55: "ラトビア語",
    56: "マオリ語",
    57: "マケドニア語",
    58: "マラヤーラム語",
    59: "マラーティー語",
    60: "マレー語",
    61: "マルタ語",
    62: "ビルマ語",
    63: "ノルウェー・ブークモール語",
    64: "ナワトル語",
    65: "ネパール語",
    66: "オランダ語",
    67: "オロモ語",
    68: "オリヤー語",
    69: "パンジャブ語",
    70: "パピアメント語",
    71: "ポーランド語",
    72: "ポルトガル語",
    73: "ピアッシュ語",
    74: "キチェ語",
    75: "ルーマニア語",
    76: "ロシア語",
    77: "シンド語",
    78: "シャン・タイヤイ語",
    79: "シンハラ語",
    80: "スロバキア語",
    81: "スロベニア語",
    82: "アルバニア語",
    83: "セルビア語",
    84: "スウェーデン語",
    85: "スワヒリ語",
    86: "タミル語",
    87: "テルグ語",
    88: "ツワナ語",
    89: "トルコ語",
    90: "タタール語",
    91: "ウルドゥー語",
    92: "ウズベク語",
    93: "ベトナム語",
    94: "中国語",
}


async def get_jp_msg_voice(
    bot_name, bot_id, message_type, input1=None, input2=None
):  # noqa: E501
    """日本語の文章を取得."""
    input1 = "" if input1 is None else str(input1)
    input2 = "" if input2 is None else str(input2)

    jp_message = {
        "help": {
            "title": "Help",
            "url": "https://gist.github.com/AlphaIru/29971af478de6a160d94571fc581db38",
            "description": f"{bot_name}の説明書です!\n\nhttps://gist.github.com/AlphaIru/29971af478de6a160d94571fc581db38\n\n(もしくはタイトルをクリックしてください)",
        },
        "username_F": {"title": "Username", "description": "これからはメッセージの作者を読み上げません!"},
        "username_T": {"title": "Username", "description": "これからはメッセージの作者を読み上げます!"},
        "botyomiage_F": {
            "title": "Read Bot",
            "description": f"これからは{bot_name}が各コマンドの文章やコメントを読み上げません!",
        },
        "botyomiage_T": {
            "title": "Read Bot",
            "description": f"これからは{bot_name}が各コマンドの文章やコメント読み上げます!",
        },
        "mention_F": {"title": "Mention", "description": "これからはメンションを読み上げません!"},
        "mention_T": {"title": "Mention", "description": "これからはメンションを読み上げます!"},
        "readotherbot_F": {
            "title": "Read Other Bot",
            "description": f"これからは{bot_name}以外のbotのメッセージを読み上げません!",
        },
        "readotherbot_T": {
            "title": "Read Other Bot",
            "description": f"これからは{bot_name}以外のbotのメッセージを読み上げます!",
        },
        "deletebotmessage_F": {
            "title": "Delete Bot Message",
            "description": f"これからは{bot_name}のメッセージを自動で削除しません!",
        },
        "deletebotmessage_T": {
            "title": "Delete Bot Message",
            "description": f"これからは{bot_name}のメッセージを自動で削除します!",
        },
        "language": {
            "title": "Language",
            "description": f"{bot_name}の言語を日本語に設定しました!",
        },
        "emoji_F": {
            "title": "Emoji",
            "description": "これからは絵文字を読み上げません!",
        },
        "emoji_T": {
            "title": "Emoji",
            "description": "これからは絵文字を読み上げます!",
        },
        "userjoin_F": {
            "title": "User Join",
            "description": "これからはユーザーがボイスチャットで操作した事を読み上げません!",
        },
        "userjoin_T": {
            "title": "User Join",
            "description": "これからはユーザーがボイスチャットで操作した事を読み上げます!",
            "em_addons": {
                0: "参加・退去",
                1: "サーバーのスピーカーミュート",
                2: "サーバーのミュート",
                3: "スピーカーミュート",
                4: "ミュート",
                5: "画面共有",
                6: "ビデオ・カメラ配信",
            },
        },
        "blacklist": {
            "title": "Blacklist",
            "description": "これからは登録したユーザーやロールをブラックリストとして取り扱います!",
        },
        "whitelist": {
            "title": "Whitelist",
            "description": "これからは登録したユーザーやロールをホワイトリストとして取り扱います!",
        },
        "readoutsideusers_F": {
            "title": "Non VC Users' Messages",
            "description": "これからはボイスチャットにいないユーザーのメッセージを読み上げません!",
        },
        "readoutsideusers_T": {
            "title": "Non VC Users' Messages",
            "description": "これからはボイスチャットにいないユーザーのメッセージを読み上げます!",
        },
        "forcejapanese_T": {
            "title": "Force Japanese",
            "description": "これからは日本語のボイスだけで読み上げます!",
        },
        "forcejapanese_F": {
            "title": "Force Japanese",
            "description": "これからは日本語のボイスだけで読み上げません!",
        },
        "voicedescription": {
            "title": "声の説明",
            "description": "英語ですが指定された声の説明を表示します!",
            "em_addons": {
                "声の名前": input1,
                "声の説明": input2,
            },
        },
        "defaultvoice": {
            "title": "Default Voice",
            "description": f"これからは{input1}のボイスが以下のデフォルト設定になります!",
            "em_addons": jp_enumrated_voices,
        },
        "editvoice": {
            "title": f"{input1}'s Voice",
            "description": f"これからは{input1}のボイスが以下の設定になります!",
            "em_addons": {
                0: "速度",
                1: "音程・音高",
                2: "言語",
                3: "ボイス名",
            },
        },
        "showvoice": {
            "title": f"{input1}'s Voice",
            "description": f"{input1}のボイスは以下の設定です!",
            "em_addons": jp_enumrated_voices,
        },
        "voiceissecret": {
            "title": f"{input1}'s Voice",
            "description": f"{input1}のボイスは秘密です!",
        },
        "showsettings": {
            "title": f"{input1}'s Settings",
            "description": f"{input1}の設定は以下の設定です!",
            "em_addons": {
                0: "ユーザー名の読み上げ",
                1: f"{bot_name}が書いた文の読み上げ",
                2: "読み上げられる文字の上限数",
                3: "絵文字の読み上げ",
                4: "メンションの読み上げ",
                5: "他のボットのメッセージの読み上げ",
                6: f"{bot_name}の文の削除",
                7: f"{bot_name}の言語",
                8: "ボイスチャットのアクティビティの読み上げ",
                9: "ホワイトリスト化",
                10: "ボイスチャットにいる人以外のユーザーのメッセージの読み上げ",
                11: "強制的にメッセージの読み上げを日本語化",
            },
        },
        "wordlimit": {
            "title": "Word Limit",
            "description": f"これからは読み上げる文字の上限数を{input1}に設定します!",
        },
        "deleteallwords": {
            "title": "Delete All Words",
            "description": "登録された辞書の単語を全て削除しました!",
        },
        "resetsettings": {
            "title": "Reset Settings",
            "description": "設定を全てリセットしました!",
        },
        "addintolist": {
            "title": f"Add into the {input2}",
            "description": f"{input1}を{input2}に追加しました!",
        },
        "removefromlist": {
            "title": f"Remove from the {input2}",
            "description": f"{input1}を{input2}から削除しました!",
        },
        "voicelist": {
            "title": "Voice List",
            "url": "https://gist.github.com/AlphaIru/c35ae3d62b6c99bc45ab4ec7a1e506a4",
            "description": f"{bot_name}で使えるボイスのリストです!\n\nhttps://gist.github.com/AlphaIru/c35ae3d62b6c99bc45ab4ec7a1e506a4",
        },
        "troubleshoot": {
            "title": "Troubleshoot",
            "description": f"{bot_name}が読み上げなくなった時の解決法です!\n基本的な解決法はこの3つ通りです!",
            "em_addons": {
                "1": f"`/reboot`で{bot_name}をボイスチャットに入れ直す!",
                "2": f"`/addchannel`で{bot_name}が読み上げるチャンネルを増やす!",
                "3": f"`/forcebye`で{bot_name}を一度強制退去させた後に`/hello`で呼び直す!",
                "これでもダメでしたら…": "それでもダメでしたら、読ませてイルカのサポートにてご連絡ください!\n[コツ: 発生条件や時間帯等と一緒に質問を頂くとありがたいです!]",
                "忠告": "サーバー側の処理落ちの可能性がありますので読み上げるまで少し待ってみてください!",
            },
        },
        "oldhello": {
            "title": "Hello",
            "description": f"恐縮ですが、{bot_name}はスラッシュコマンドの完全移行の関係でこのコマンドはもう使えません!\n今後は `/hello` で召喚してください!",
            "em_addons": {
                "**招待リンク**": "スラコマを使用するにはBotをサーバーに再召喚する可能性があります! 以下のリンクをクリックして再召喚してください!",
                "**Iru**": r"https://discord.com/api/oauth2/authorize?client_id=813401103270019102&permissions=36826448&scope=bot%20applications.commands",
                "**Ruka**": r"https://discord.com/api/oauth2/authorize?client_id=820128974176649266&permissions=36826448&scope=bot%20applications.commands",
                "**Dolun**": r"https://discord.com/api/oauth2/authorize?client_id=906641565441736744&permissions=36826448&scope=bot%20applications.commands",
                "**Finta**": r"https://discord.com/api/oauth2/authorize?client_id=906641635092332586&permissions=36826448&scope=bot%20applications.commands",
                "**Cete**": r"https://discord.com/api/oauth2/authorize?client_id=906643085264572426&permissions=36826448&scope=bot%20applications.commands",
                "**Official Discord Server**": "https://discord.gg/PBJ6969J2S",
            },
        },
        "ping": {
            "title": "Pong",
            "description": f"{bot_name}がコマンドの受け取りとその処理でかかった時間を表示します!",
            "em_addons": {
                "Latency": f"Latency時間は`{input1}ms`です!",
                "Process": f"Process時間は`{input2}ms`です!",
            },
        },
        "credit": {
            "title": "Credit",
            "description": f"{bot_name}の作成に関わってくれた機関や人達です!どうかこの人達を先に感謝してください!",
            "em_addons": {
                "製作者からのお礼": "秘密のコマンドを見つけてくれてありがとうございます!これを作成するのにどれだけの人や機関に頼ってきたか自分でもはっきりとスケールが取れていません!彼らに感謝の気持ちでいっぱいですが、使ってくれてる皆さん方にも感謝しています!これからも読ませてイルカの改善等に努力します!お付き合いありがとうございます!ありがとうございました!:heart:",
                "読ませてイルカの管理": "**・Airun**",
                "読ませてイルカのコアやエンジン": "**・**TogeRaz \n**・**Tom_XV \n**・**Baku_reshi\n**・**Yuki_Trans \n**・Alpha_Iru**",
                "スペシャルサンクス": "**・**Kazu220_ps \n**・**Wilco \n**・**Sunnyong \n**・**Jun (Lyreon) \n**・TheCorgiDoggo** \n**・**Nemy_zz \n**・**Yhay81 \n**・**cod",
                "Early Alpha Testers/Servers": "**・**アモングアス鯖(ポケモン勢): owned by Shaurufu \n**・**[Corn's Keyboard Mashers](https://discord.gg/mv8umv5brA): owned by TheCorgiDoggo \n**・**とあるオタクの緊急会議: owned by 1nRqnsh11n \n**・**Latios's Skybase: owned by Jun \n**・**[せかんど☆えでん](https://discord.gg/53G8RcqH4S): owned by Tera_Katzen \n**・**[げーみんぐ](https://discord.gg/nuBhDrN2xh): owned by yuureighost",
                "Open_JTalk (日本語読み上げエンジン)": "**・**Keiichi Tokuda \n**・**Keiichiro Oura \n**・**Kei Hashimoto \n**・**Sayaka Shiota \n**・**Shinji Takaki \n**・**Heiga Zen \n**・**Junichi Yamagishi \n**・**Tomoki Toda \n**・**Takashi Nose \n**・**Shinji Sako \n**・**Alan W. Black \n**・**Some Graduate Students from Nagoya Institute of Technology Department of Computer Science \n ",
                "Mei声": "**・**Keiichi Tokuda \n**・**Akinobu Lee \n**・**Keiichiro Oura \n**・**Daisuke Yamamoto",
                "Tohoku声": "Tohoku University Graduate School of Engineering Department of Communication Engineering Ito/Nose Laboratory",
                "Flite (英語読み上げエンジン)": "**・**Alan W. Black \n**・**Kevin A. Lenzo \n**・**Carnegie Mellon University \n**・**University of Edinburgh",
                "Alkana (英語ローマ字化エンジン)": "**・**Cod",
                "Bep-Eng.dic (ローマ字辞書)": "**・**M.Ohtsuka(mash)",
                f"{bot_name}のプロフィール画像": "**・**Alpha_Iru \n**・**Kam",
                "利用規約&ライセンス": "**・**[Flite](https://github.com/festvox/flite/blob/master/COPYING) \n**・**[Open_JTalk](http://open-jtalk.sourceforge.net/readme_open_jtalk.php) \n**・**[MMDAgent](https://mmdagent-ex.dev/ja/docs/term/termofservice) \n**・**[Tohoku_Voice](https://github.com/icn-lab/htsvoice-tohoku-f01/blob/master/COPYRIGHT.txt)",
            },
        },
        "hello": {
            "title": "Hello",
            "description": f"{bot_name}がボイスチャットに入りました!これからの文章を読み上げます!",
            "em_addons": {
                "**Bot Link**": "Botの招待リンクは次のコマンドを打ってください!:\n``/bot_discord_link``",
                "**Official Discord Server**": "https://discord.gg/PBJ6969J2S",
            },
        },
        "byenow": {
            "title": "Bye",
            "description": f"{bot_name}がボイスチャットから出ました!ご利用ありがとうございました!",
            "em_addons": {
                "**Official Discord Server**": "https://discord.gg/PBJ6969J2S",
            },
        },
        "byelater": {
            "title": "Bye",
            "description": f"{bot_name}がボイスチャットから出ます!すべて読み上げるまで{bot_name}はここにいます。ご利用ありがとうございました!",
            "em_addons": {
                "**Official Discord Server**": "https://discord.gg/PBJ6969J2S",
            },
        },
        "forcedisconnect": {
            "title": "Force Disconnect",
            "description": f"{bot_name}が強制的にボイスチャットから出ました!",
        },
        "stop": {
            "title": "Stop",
            "description": f"只今、{bot_name}が読み上げを停止しました!",
        },
        "pause": {
            "title": "Pause",
            "description": f"只今、{bot_name}が読み上げを一時停止しました!",
        },
        "resume": {
            "title": "Resume",
            "description": f"{bot_name}が読み上げを再開しました!",
        },
        "reboot": {
            "title": "Reboot",
            "description": f"{bot_name}が再起動しました!",
        },
        "move": {
            "title": "Move",
            "description": f"{bot_name}が{input1}に移動しました!",
        },
        "send": {
            "title": "Send",
            "description": f"{bot_name}が{input1}に移動しました!",
        },
        "addword": {
            "title": "Add Word",
            "description": f"{bot_name}が{input1}を{input2}として辞書に登録しました!",
            "em_addons": {
                "Length Warning": "単語数が長すぎましたので、単語の後方部の方を切り落として登録しました。",
            },
        },
        "reword": {
            "title": "Add Word",
            "description": f"{bot_name}が{input1}を{input2}として辞書に登録し直しました!",
            "em_addons": {
                "Length Warning": "単語数が長すぎましたので、単語の後方部の方を切り落として登録しました。",
            },
        },
        "importfile": {
            "title": "Import",
            "description": f"先程のファイルから合計{input1}の単語を辞書に登録しました!",
            "em_addons": {
                0: {"注意": "-------------------------------------\n"},
                1: {
                    "**・辞書内と同じ単語 (ファイル外重複)**": "ファイル中にある単語と辞書内の単語の中に同じ単語が複数ありましたのでファイルにある単語の読み方として上書きしました!",
                },
                2: {
                    "**・ファイル内に同じ単語 (ファイル内重複)**": "ファイル中にある単語の中に同じ単語が複数ありましたのでファイルの下部にある読み方は登録されていません!",
                },
                3: {
                    "**・単語と読み方が同じ (読み方重複)**": "ファイル中にある単語の中に単語とその読み方が同じ単語がありましたのでその単語は追加されてません!",
                },
                4: {
                    "**・単語の長さ**": "ファイル中にある単語で文字数が長い単語がありましたのでその単語の後方部は抜かれた状態で登録してあります!",
                },
                5: {"**・読み方不足**": "ファイル中に読み方が無い単語がありました!その単語は登録されていません!"},
                6: {
                    "**・登録されてる単語の数**": "元々登録されてた単語の数が多くありましたのでファイルの下方を優先的にある単語は追加されていません!",
                },
                7: {"**・単語のタイプ**": "ファイルの中にある単語がStringではありませんでした!"},
            },
        },
        "exportfile": {
            "title": "Export",
            "description": f"{bot_name}が辞書をファイルにエクスポートしました!",
            "em_addons": {
                "ファイルのインフォメーション": f"ファイルの拡張子は `{input1}`, ファイルのサイズは `{input2} Bytes` です!",
            },
        },
        "deleteword": {
            "title": "Delete Word",
            "description": f"{bot_name}が{input1}を辞書から削除しました!",
        },
        "botdiscordlink": {
            "title": "Bot Discord Link",
            "url": "https://discord.gg/PBJ6969J2S",
            "description": f"各Botのリンクや{bot_name}の公式Discordサーバーのリンクです!",
            "em_addons": {
                "**Iru**": r"https://discord.com/api/oauth2/authorize?client_id=813401103270019102&permissions=36826448&scope=bot%20applications.commands",
                "**Ruka**": r"https://discord.com/api/oauth2/authorize?client_id=820128974176649266&permissions=36826448&scope=bot%20applications.commands",
                "**Dolun**": r"https://discord.com/api/oauth2/authorize?client_id=906641565441736744&permissions=36826448&scope=bot%20applications.commands",
                "**Finta**": r"https://discord.com/api/oauth2/authorize?client_id=906641635092332586&permissions=36826448&scope=bot%20applications.commands",
                "**Cete**": r"https://discord.com/api/oauth2/authorize?client_id=906643085264572426&permissions=36826448&scope=bot%20applications.commands",
                "**Official Discord Server**": "https://discord.gg/PBJ6969J2S",
            },
        },
        "addchannel": {
            "title": "Add Channel",
            "description": f"次から{input1}を読み上げます!",
            "em_addons": {
                "読み上げるチャンネル: ": input2,
            },
        },
        "byechannel": {
            "title": "Bye",
            "description": f"読み上げるチャンネルがなくなりましたので{bot_name}がボイスチャットから出ました!ご利用ありがとうございました!",
        },
        "removechannel": {
            "title": "Remove Channel",
            "description": f"次から{input1}を読み上げません!",
            "em_addons": {
                "読み上げるチャンネル: ": input2,
            },
        },
        "botmention": {
            "title": bot_name,
            "description": f"{bot_name}のヘルプコマンドは[/help]です!",
        },
        "byevoicesingle": {
            "title": "Bye",
            "description": f"ボイスチャンネルに誰もいなくなりましたので{bot_name}がボイスチャットから出ました!ご利用ありがとうございました!",
        },
        "byevoicebot": {
            "title": "Bye",
            "description": f"ボイスチャンネルにBotしかいなくなりましたので{bot_name}がボイスチャットから出ました!ご利用ありがとうございました!",
        },
        "byeforce": {
            "title": "Bye",
            "description": f"強制退去のコマンドを受け取りました!不安定になる可能性があるのでできるなら避けていただきたいです。しかしながら{bot_name}のご利用ありがとうございました!",
        },
        "byeafk": {
            "title": "Bye",
            "description": f"{bot_name}がAFKになっていたのでボイスチャットから出ました!ご利用ありがとうございました!",
        },
        # -------------------------
        "missingvoice": {
            "title": "Error",
            "description": "設定したボイスは存在しません!",
        },
        "nowordsindictionary": {
            "title": "Error",
            "description": "辞書に単語が一つもありません!",
        },
        "toomuchinlist": {
            "title": "Error",
            "description": f"{input2}が満杯です!{input1}を足す前にいくつか外してください!",
        },
        "repeatinlist": {
            "title": "Error",
            "description": f"{input1}は既に{input2}で登録されています!",
        },
        "notinlist": {
            "title": "Error",
            "description": f"{input1}は{input2}に登録されていません!",
        },
        "usernotconnected": {
            "title": "Error",
            "description": "ユーザーがボイスチャットに接続されていません!",
        },
        "alreadyconnected": {
            "title": "Error",
            "description": f"{bot_name}は既にボイスチャットに接続されています!",
        },
        "otherdolphinconnected": {
            "title": "Error",
            "description": "他のイルカがつながっています!その子を使ってあげてください!",
        },
        "fullservice": {
            "title": "Error",
            "description": f"今、{bot_name}がフル稼働中です!後でもう一度お試しください!",
        },
        "toomanymembers": {
            "title": "Error",
            "description": "ボイスチャットの人数上限に達しています!後でもう一度お試しください!",
        },
        "notfinishedreading": {
            "title": "Error",
            "description": "読み上げ中です!終了してからもう一度お試しください!",
        },
        "notenoughpermission": {
            "title": "Error",
            "description": f"{bot_name}がこのボイスチャットに入る為の権限がありません!\n\nアドミンから「チャンネルを見る」, 「接続」, 「話す」の権限が必要です!",
        },
        "notconnected": {
            "title": "Error",
            "description": f"{bot_name}はボイスチャットに接続されていません!",
        },
        "notreading": {
            "title": "Error",
            "description": f"只今、{bot_name}は読み上げ中ではありません!",
        },
        "alreadypaused": {
            "title": "Error",
            "description": f"只今、{bot_name}は読み上げを一時停止しています!",
        },
        "alreadyresumed": {
            "title": "Error",
            "description": f"只今、{bot_name}は読み上げを再開しています!",
        },
        "notenoughmembers": {
            "title": "Error",
            "description": "ボイスチャットに誰もいません!",
        },
        "samewords": {
            "title": "Error",
            "description": "入力された単語が同じです!",
        },
        "overdic": {
            "title": "Error",
            "description": "辞書に登録された単語が多すぎます!",
        },
        "filesizetoobig": {
            "title": "Error",
            "description": "ファイルサイズが大きすぎます!",
        },
        "fileextensionerror": {
            "title": "Error",
            "description": "そのファイル拡張子はサポートしていません!",
            "em_addons": {
                "**サポートしてる拡張子:**": "`.txt` `.csv` `.dict`",
            },
        },
        "filecorrupted": {
            "title": "Error",
            "description": "ファイルが読み込めませんでした!壊れている可能性があります!",
        },
        "filetypeerror": {
            "title": "Error",
            "description": "ファイルの中身にある単語がStringではありませんでした!",
        },
        "noword": {
            "title": "Error",
            "description": "辞書に指定された単語はありません!",
        },
        "toomanychannels": {
            "title": "Error",
            "description": f"読み上げるメッセージチャンネルが多すぎます!{input1}を足す前にいくつか外してください!",
        },
        "channelalreadyadded": {
            "title": "Error",
            "description": f"{input1}は既に読み上げるメッセージチャンネルに登録されています!",
        },
        "channelnotadded": {
            "title": "Error",
            "description": f"{input1}は読み上げるメッセージチャンネルに登録されていません!",
        },
        "missingarguments": {
            "title": "Error",
            "description": "このコマンドを使用するために必要な要件が足りません!",
        },
        "botmissingpermissions": {
            "title": "Error",
            "description": f"このコマンドを使用する為の{bot_name}に必要な権限がありません!",
        },
        "cooldown": {
            "title": "Error",
            "description": f"コマンドの送りすぎです! このコマンドは{input1}秒後に使用できます!",
        },
        "missingpermissions": {
            "title": "Error",
            "description": "このコマンドを使用する為のユーザーが必要な権限がありません!",
        },
        "userinputerror": {
            "title": "Error",
            "description": "入力した値が不正です!再度ご確認ください!",
        },
        "notadmin": {
            "title": "Error",
            "description": "このコマンドを使用する為のアドミン権限がありません!",
        },
        "inblacklist": {
            "title": "Blacklist",
            "description": "ブラックリストに登録されています!そのコマンドは無視されます!",
        },
        "notinwhitelist": {
            "title": "Whitelist",
            "description": "ホワイトリストに登録されていません!そのコマンドは無視されます!",
        },
        "botbored": {
            "title": "Error",
            "description": f"{bot_name}は今、暇そうにしています!",
        },
        "unknownerror": {
            "title": "Error",
            "description": "深刻なエラーが発生しました! このエラーをイルカの住処に報告してください!",
            "em_addons": {
                "エラーの名前: ": type(input1).__name__,
                "エラーの説明: ": str(input1)
            },
        },
    }

    jp_voice_iru = {
        "help": "僕達、読ませてイルカの説明書に飛ぶリンクだよ!ここでコマンドとか確認してね～!",
        "username_F": "これからはメッセージの作者を読み上げないよ～!",
        "username_T": "これからはメッセージの作者を読み上げるよ～!",
        "botyomiage_F": "これからは僕の文章を読み上げないよ～!(悲しいなあ…)",
        "botyomiage_T": "これからは僕の文章を読み上げるよ～!(ありがとう!)",
        "mention_F": "これからはメンションを読み上げないよ～!",
        "mention_T": "これからはメンションを読み上げるよ～!",
        "readotherbot_F": "これからは僕以外のbotのメッセージを読み上げないよ～!",
        "readotherbot_T": "これからは僕以外のbotのメッセージを読み上げるよ～!",
        "deletebotmessage_F": "これからは僕のメッセージを自動で削除しないよ～!",
        "deletebotmessage_T": "これからは僕のメッセージを自動で削除するよ～!",
        "language": "こんにちは～!日本語に設定したよ～!",
        "emoji_F": "これからは絵文字を読み上げないよ～!",
        "emoji_T": "これからは絵文字を読み上げるよ～!",
        "userjoin_F": "これからはユーザーがボイスチャットでのアクションを読み上げないよ～!",
        "userjoin_T": "これからはユーザーがボイスチャットでのアクションを読み上げるよ～!",
        "blacklist": "これからは登録したユーザーやロールをブラックリストとして取り扱うよ～!",
        "whitelist": "これからは登録したユーザーやロールをホワイトリストとして取り扱うよ～!",
        "readoutsideusers_F": "これからはボイスチャットにいないユーザーのメッセージを読み上げないよ～!",
        "readoutsideusers_T": "これからはボイスチャットにいないユーザーのメッセージを読み上げるよ～!",
        "forcejapanese_T": "これからは日本語のボイスだけで読み上げるよ～!",
        "forcejapanese_F": "これからは日本語のボイスだけで読み上げないよ～!",
        "voicedescription": "選んだ声の説明を出すよ～!",
        "defaultvoice": f"これからは{input1}のボイスがこのデフォルト設定になるよ～!",
        "editvoice": f"これからは{input1}のボイスがこの設定になるよ～!",
        "showvoice": f"{input1}のボイスは以下の設定だよ～!",
        "voiceissecret": "僕の声は、ひ、み、つ、だよ！",
        "showsettings": f"{input1}の設定は以下の設定だよ～!",
        "wordlimit": f"これからは読み上げる文字数の上限数を{input1}に設定するよ～",
        "deleteallwords": "登録された辞書の単語を全て削除したよ～!",
        "resetsettings": "設定を全てリセットしたよ～!",
        "addintolist": f"{input1}を{input2}に追加したよ～!",
        "removefromlist": f"{input1}を{input2}から削除したよ～!",
        "voicelist": "僕が言えるボイスだよ!色々と試してね!",
        "troubleshoot": "僕が何も言わなくなった時の対処法だよ!まずは以下の通りを試してみてね!",
        "oldhello": "長い間使ってくれてありがとう!これからもよろしくね!",
        "ping": f"僕がそのコマンドを受け取った時間は{input1}ミリセカンドでそれを処理に掛かった時間は{input2}ミリセカンドだよ!",
        "credit": "僕の作者は以下の人達だよ～!みんなにお礼を言ってね、僕からもみんなにありがとう!",
        "hello": "こんにちは!僕はイルカのイルーだよ!これからの文章を読み上げるね!よろしく!",
        "byenow": "ありがとう!僕抜けるね!またね!",
        "byelater": "最後までありがとう!僕抜けるね!またね!",
        "forcedisconnect": "僕が強制的に抜けたよ!これでバグ直ったかな?",
        "stop": "今、読み上げを停止したよ!",
        "pause": "今、読み上げを一時停止したよ!",
        "resume": "今、読み上げを再開したよ!",
        "reboot": "今、入り直したよ!",
        "move": f"今、{input1}に移動したよ!",
        "send": f"今、{input1}に移動したよ!",
        "addword": f"{input1}を辞書に単語を登録したよ!",
        "reword": f"{input1}を辞書に単語を登録し直したよ!",
        "importfile": "ファイルから単語を辞書にインポートしたよ!",
        "exportfile": "辞書から単語をファイルにエクスポートしたよ!",
        "deleteword": f"辞書から{input1}を削除したよ!",
        "botdiscordlink": "僕達を呼ぶリンクやDiscordサーバーのリンクだよ!暇だったら来てみてね～!",
        "addchannel": f"これからは{input1}のメッセージを読み上げるよ～!",
        "byechannel": "読み上げるチャンネルが無くなったから僕抜けるね!またね！",
        "removechannel": f"これからは{input1}のメッセージを読み上げないよ～!",
        "botmention": "ヘルプはスラッシュヘルプって入れてね!",
        "byevoicesingle": "ボイチャに誰もいなくなったから僕抜けたよ～!またね！",
        "byevoicebot": "ボイチャにBotしかいなくなったから僕抜けたよ～!またね！",
        "byeforce": "ボイチャから強制的に抜けたよ～!またね！",
        "byeafk": "AFKだったからボイチャから抜けたよ～!またね！",
        # -----
        "missingvoice": "設定したボイスは存在しません～!シランガナ!",
        "nowordsindictionary": "辞書に単語が一つも無いよ～!シランガナ!",
        "toomuchinlist": f"{input2}が満杯だよ!{input1}を足す前にいくつか外してね!シランガナ!",
        "repeatinlist": f"{input1}はもう{input2}で登録されているよ!シランガナ!",
        "notinlist": f"{input1}は{input2}に登録されていないよ!シランガナ!",
        "usernotconnected": "誰かが僕を呼ぼうとしてるよ!シランガナ!",
        "alreadyconnected": "僕、もうボイチャにつながってるよ!シランガナ!",
        "otherdolphinconnected": "僕の友達がもう繋がってるよ!その子に任せてね!",
        "fullservice": "今、空いてる手が無いよ!シランガナ!",
        "toomanymembers": "ボイチャの人数上限に達しているよ!シランガナ!",
        "notfinishedreading": "まだ読み終わってないよ!シランガナ!",
        "notenoughpermission": "ボイチャに入る為の権限がないよ!シランガナ!",
        "notconnected": "僕、ボイチャにつながってないよ!シランガナ!",
        "notreading": "今、何も読み上げてないよ!シランガナ!",
        "alreadypaused": "今、読み上げを一時停止してるよ!シランガナ!",
        "alreadyresumed": "今、読み上げてるよ!シランガナ!",
        "notenoughmembers": "ボイチャに誰もいないよ!シランガナ!",
        "samewords": "同じ単語だよ!シランガナ!",
        "overdic": "辞書にある単語が多すぎるよ!シランガナ!",
        "filesizetoobig": "ファイルサイズが大きすぎるよ!シランガナ!",
        "fileextensionerror": "ファイル拡張子がサポートされてないよ!シランガナ!",
        "filecorrupted": "ファイルが壊れてる可能性があるよ!シランガナ!",
        "filetypeerror": "ファイルの中身がStringじゃなかったよ!シランガナ!",
        "noword": "そんな単語は登録されていないよ!シランガナ!",
        "toomanychannels": f"読み上げるメッセージチャンネルが多すぎるよ!{input1}を足す前にいくつか外してね!シランガナ!",
        "channelalreadyadded": f"{input1}はもう読み上げるメッセージチャンネルに登録されているよ!シランガナ!",
        "channelnotadded": f"{input1}は読み上げるメッセージチャンネルに登録されていないよ!シランガナ!",
        "missingarguments": "このコマンドに必要な要件が足りないよ!シランガナ!",
        "botmissingpermissions": "このコマンドに必要な権限が僕には無いよ!シランガナ!",
        "cooldown": f"コマンドの送り過ぎだよ! ちょっと{input1}秒まってね!",
        "missingpermissions": "このコマンドに必要な権限が君には無いよ!シランガナ!",
        "userinputerror": "入力内容がおかしいよ!シランガナ!",
        "notadmin": "管理者権限がないよ!シランガナ!",
        "inblacklist": "ブラックリストに登録されてるよ!シランガナ!",
        "notinwhitelist": "ホワイトリストに登録されてないよ!シランガナ!",
        "botbored": "つまんないよ!シランガナ!",
        "unknownerror": "このエラーをすぐに報告してね!",
    }

    jp_voice_ruka = {
        "help": "わ、私達の…、よ、読ませてイルカの…、せ、説明書に…、飛ぶ…、リンクです。こ、ここで確認を…、お、お願いします！",
        "username_F": "こ、これからは…、メッセージの…、さ、作者さんを…、よ、読み上げ…、ません!",
        "username_T": "こ、これからは…、メッセージの…、さ、作者さんを…、よ、読み上げ…、ます!",
        "botyomiage_F": "こ、これからは…、私の文章を…、よ、読み上げ…、ません!(ほ…)",
        "botyomiage_T": "こ、これからは…、私の文章を…、よ、読み上げ…、ます!(よ、よろしく…、お願いします!)",
        "mention_F": "こ、これからは…、メンションを…、よ、読み上げ…、ません!",
        "mention_T": "こ、これからは…、メンションを…、よ、読み上げ…、ます!",
        "readotherbot_F": "こ、これからは…、私以外の…、ボットのメッセージを…、よ、読み上げ…、ません!",
        "readotherbot_T": "こ、これからは…、私以外の…、ボットのメッセージを…、よ、読み上げ…、ます!",
        "deletebotmessage_F": "こ、これからは…、私の…、め、メッセージを…、け、消しません!",
        "deletebotmessage_T": "こ、これからは…、私の…、め、メッセージを…、け、消します!",
        "language": "こ、こんにちは。に、日本語に…、設定…、し、しました。よ、よろしく…、お願いします!",
        "emoji_F": "こ、これからは…、絵文字を…、よ、読み上げ…、ません!",
        "emoji_T": "こ、これからは…、絵文字を…、よ、読み上げ…、ます!",
        "userjoin_F": "こ、これからは…、ボイスチャットで起きた…、出来事を…、よ、読み上げ…、ません!",
        "userjoin_T": "こ、これからは…、ボイスチャットで起きた…、出来事を…、よ、読み上げ…、ます!",
        "blacklist": "こ、これからは…、登録したユーザーやロールを…、ブラックリストとして…、と、取り扱います!",
        "whitelist": "こ、これからは…、登録したユーザーやロールを…、ホワイトリストとして…、と、取り扱います!",
        "readoutsideusers_F": "こ、これからは…、ボイスチャットにいない…、ユーザーのメッセージを…、よ、読み上げ…、ません!",
        "readoutsideusers_T": "こ、これからは…、ボイスチャットにいない…、ユーザーのメッセージを…、よ、読み上げ…、ます!",
        "forcejapanese_T": "こ、これからは…、日本語のボイスだけで…、よ、読み上げ…、ます!",
        "forcejapanese_F": "こ、これからは…、日本語のボイスだけで…、よ、読み上げ…、ません!",
        "voicedescription": "え、選んだ声の…、せ、説明を…、出します!",
        "defaultvoice": f"こ、これからは…、{input1}のボイスが…、デフォルトの設定と…、な、なります!",
        "editvoice": f"こ、これからは…、{input1}、のボイスが…、以下の設定と…、な、なります!",
        "showvoice": f"{input1}のボイスは…、い、以下の通りです!",
        "voiceissecret": "わ、私の声は…、ひ、秘密です!(は、恥ずかしいので…、き、聞かないでください!)",
        "showsettings": f"{input1}の設定は…、い、以下の通りです!",
        "wordlimit": f"こ、これからは…、よ、読み上げる文字数の…、上限数を{input1}文字に…、せ、設定します!",
        "deleteallwords": "こ、このサーバーの辞書に…、登録されてる単語を…、全て削除しました!",
        "resetsettings": "こ、このサーバーの設定を…、す、全てリセットしました!",
        "addintolist": f"{input1}を…、{input2}に…、つ、追加しました!",
        "removefromlist": f"{input1}を…、{input2}から…、は、外しました!",
        "voicelist": "わ、私が扱える…、ボイスです!ど、どうぞ、色々と試して…、く、ください!",
        "troubleshoot": "わ、私が何か…、失敗した時の…、対処法です!い、以下の順に、試して…、く、ください!",
        "oldhello": "そ、そのコマンドは…、もう使えません!す、スラッシュコマンドで呼んで…、く、ください!",
        "ping": f"わ、私がそのコマンドを…、受け取った時間は…、{input1}ミリ秒で…、そ…、それの処理に掛かった時間は…、{input2}ミリ秒です!",
        "credit": "わ、私達の親です!う、うちらを…、選んでいただき…、あ、ありがとう、ございます!",
        "hello": "あ、こ、こんにちはです!わ、私は…、ベルーガの、る、ルカです!こ、これからの文章を、読み上げ…、ます!よ、よろしく…、お願いします!",
        "byenow": "わ、私…、し、失礼します!あ、ありがとう、ございました!",
        "byelater": "わ、私…、し、失礼します!さ、最後まで…、あ、ありがとう、ございました!",
        "forcedisconnect": "きょ、強制的に…、お、降りました!だ、大丈夫でしょうか?",
        "stop": "い、今、よ、読み上げを…、て、停止しました!",
        "pause": "い、今、よ、読み上げを…、い、一時停止しました!",
        "resume": "い、今、よ、読み上げを…、再開しました!",
        "reboot": "い、今、入り直し…、し、しました!",
        "move": f"い、今、{input1}に…、移動しました!",
        "send": f"い、今、{input1}に…、移動しました!",
        "addword": f"{input1}を辞書に…、と、登録しました!",
        "reword": f"{input1}を辞書に…、と、登録し直しました!",
        "importfile": "か、各単語を…、ファイルから辞書に…、い、インポートしました!",
        "exportfile": "か、各単語を…、辞書からファイルに…、え、エクスポートしました!",
        "deleteword": f"じ、辞書から、{input1}を、外しました!",
        "botdiscordlink": "わ、私達を呼ぶリンクと…、私達の…、ディスコードサーバーの…、り、リンクです!よ、よろしく…、お願いします!",
        "addchannel": f"こ、これからは…、{input1}のメッセージを、よ、読み上げます!",
        "byechannel": "よ、読み上げるチャンネルが…、無くなりましたので、し、失礼します!",
        "removechannel": f"こ、これからは…、{input1}の…、メッセージを…、よ、読み上げません!",
        "botmention": "へ、ヘルプなら…、スラッシュヘルプと…、お、送ってください!",
        "byevoicesingle": "ぼ、ボイスチャットに…、誰もいなくなったので…、し、失礼します!",
        "byevoicebot": "ぼ、ボイスチャットに…、ボットしか…、いなくなったので…、し、失礼します!",
        "byeforce": "きょ、強制的に、ぼ、ボイス、ちゃ、チャット、か、から、おり、降りました!し、失礼、し、しました!",
        "byeafk": "え、エーエフケーでしたので…、ボイスチャットから…、し、失礼します!",
        # -----
        "missingvoice": "せ、設定したボイスは…、そ、存在しません!",
        "nowordsindictionary": "じ、辞書に単語が…、一つも…、あ、ありません!",
        "toomuchinlist": f"{input2}は只今…、満杯です!{input1}を足す前に…、い、いくつか外してください!",
        "repeatinlist": f"{input1}はすでに…、{input2}に登録されています!",
        "notinlist": f"{input1}は…、{input2}に…、と、登録されていません!",
        "usernotconnected": "だ、誰かが私を…、よ、呼ぼうとしています!",
        "alreadyconnected": "わ、私はすでに、ぼ、ボイス、ちゃ、チャットに、つ、繋がって、い、います!",
        "otherdolphinconnected": "わ、私の、と、友達が、す、すでに、つ、繋がって、い、います!",
        "fullservice": "い、今、あ、空いてる、て、手が、あ、ありません!",
        "toomanymembers": "ぼ、ボイス、ちゃ、チャットの、に、人数、じょ、上限に、た、達して、い、います!",
        "notfinishedreading": "ま、まだ、よ、読み、お、終わって、い、いません!",
        "notenoughpermission": "ぼ、ボイス、ちゃ、チャットに、入る、た、為の、け、権限が、あ、ありません!",
        "notconnected": "わ、私、ぼ、ボイス、ちゃ、チャットに、つ、繋がって、い、いません!",
        "notreading": "わ、私、い、今、な、何も、よ、読み、あ、上げて、い、いません!",
        "alreadypaused": "わ、私、い、今、よ、読み、あ、上げを、い、一時、て、停止、し、しています!",
        "alreadyresumed": "い、今、よ、読み、あ、上げて、い、います!",
        "notenoughmembers": "ぼ、ボイス、ちゃ、チャットに、だ、誰も、い、いません!",
        "samewords": "お、同じ、た、単語です!",
        "overdic": "じ、辞書に、あ、ある、た、単語が、お、多すぎます!",
        "filesizetoobig": "ふぁ、ファイル、さ、サイズが、お、大きすぎます!",
        "fileextensionerror": "ふぁ、ファイル、か、拡張子が、さ、サポート、さ、されて、い、いません!",
        "filecorrupted": "ふぁ、ファイルが、こ、壊れてる、か、可能性が、あ、あります!",
        "filetypeerror": "ふぁ、ファイルの、な、中身が、す、String、で、では、あ、ありません!",
        "noword": "そ、そんな、た、単語は、と、登録、さ、されて、い、いません!",
        "toomanychannels": f"よ、読み、あ、上げる、め、メッセージ、ちゃ、チャンネルが、お、多すぎます!{input1}を、た、足す前に、い、いくつか、外して、く、ください!",
        "channelalreadyadded": f"{input1}は、も、もう、よ、読み、あ、上げる、め、メッセージ、ちゃ、チャンネルに、と、登録、さ、されて、い、います!",
        "channelnotadded": f"{input1}は、よ、読み、あ、上げる、め、メッセージ、ちゃ、チャンネルに、と、登録、さ、されて、い、いません!",
        "missingarguments": "こ、この、こ、コマンドに、ひ、必要な、よ、要件が、た、足りません!",
        "botmissingpermissions": "こ、この、こ、コマンドに、ひ、必要な、け、権限が、た、足りません!",
        "cooldown": f"こ、コマンドの、お、送り、す、過ぎです! ちょ、ちょっと、と、{input1}秒、ま、まってね!",
        "missingpermissions": "こ、この、こ、コマンドに、ひ、必要な、け、権限が、あ、ありません!",
        "userinputerror": "にゅ、入力、な、内容が、お、おかしいです!も、もう一度、か、確認して、にゅ、入力して、く、ください!",
        "notadmin": "か、管理者、け、権限が、あ、ありません!",
        "inblacklist": "ぶ、ブラック、り、リストに、と、登録、さ、されて、い、います!",
        "notinwhitelist": "ほ、ホワイト、り、リストに、と、登録、さ、されて、い、いません!",
        "botbored": "す、少し、あ、遊び、た、たいです!",
        "unknownerror": "こ、このエラーをすぐに、ほ、報告してください!",
    }

    jp_voice_dolun = jp_voice_iru
    jp_voice_finta = jp_voice_iru
    jp_voice_cete = jp_voice_iru

    async def id_to_voice(bot_id):
        if bot_id == 813401103270019102 or not bot_id:
            return jp_voice_iru[message_type]
        elif bot_id == 820128974176649266:
            return jp_voice_ruka[message_type]  # jp_voice_Ruka[message_type]
        elif bot_id == 906641565441736744:
            return jp_voice_dolun[message_type]
        elif bot_id == 906641635092332586:
            return jp_voice_finta[message_type]
        elif bot_id == 906643085264572426:
            return jp_voice_cete[message_type]
        else:
            return jp_voice_iru[message_type]

    return jp_message[message_type], await id_to_voice(bot_id)


# pylint: enable=line-too-long
