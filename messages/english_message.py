# coding: utf-8
"""英語の文章などを取得."""
# pylint: disable=line-too-long
# pylama: ignore=E501


en_enumrated_voices = {
    0: "Speed",
    1: "Pitch",
    2: "Afrikaans",
    3: "Amharic",
    4: "Aragonese",
    5: "Arabic",
    6: "Assamese",
    7: "Azebaijani",
    8: "Bashkir",
    9: "Bulgarian",
    10: "Bengali",
    11: "Bishnupriy Manipuri",
    12: "Breton",
    13: "Bosnian",
    14: "Catalan",
    15: "Czech",
    16: "Welsh",
    17: "Danish",
    18: "German",
    19: "Greek",
    20: "English",
    21: "Esperanto",
    22: "Spanish",
    23: "Estonian",
    24: "Basque",
    25: "Persian",
    26: "Finnish",
    27: "French",
    28: "Irish Gaelic",
    29: "Scottish Gaelic",
    30: "Guaraní",
    31: "Gujarati",
    32: "Hebrew",
    33: "Hindi",
    34: "Croatian",
    35: "Hatian Creole",
    36: "Hungarian",
    37: "Armenian",
    38: "Interlingua",
    39: "Indonesian",
    40: "Icelandic",
    41: "Italian",
    42: "Lojban",
    43: "Japanese",
    44: "Georgian",
    45: "Kazakh",
    46: "Greenlandic",
    47: "Kannada",
    48: "Korean",
    49: "Konkani",
    50: "Kurdish Kurmanji",
    51: "Kyrgyz",
    52: "Latin",
    53: "Lingua Franca Nova",
    54: "Lithuanian",
    55: "Latvian",
    56: "Maori",
    57: "Macedonian",
    58: "Malayalam",
    59: "Marathi",
    60: "Malay",
    61: "Maltese",
    62: "Myanmar (Burmese)",
    63: "Norwegian Bokmål",
    64: "Nahuatl (Classical)",
    65: "Nepali",
    66: "Dutch",
    67: "Oromo",
    68: "Oriya",
    69: "Punjabi",
    70: "Papiamento",
    71: "Polish",
    72: "Portuguese",
    73: "Pyash",
    74: "K'iche'",
    75: "Romanian",
    76: "Russian",
    77: "Sindhi",
    78: "Shan (Tai Yai)",
    79: "Sinhala",
    80: "Slovak",
    81: "Slovenian",
    82: "Albanian",
    83: "Serbian",
    84: "Swedish",
    85: "Swahili",
    86: "Tamil",
    87: "Telugu",
    88: "Setswana",
    89: "Turkish",
    90: "Tatar",
    91: "Urdu",
    92: "Uzbek",
    93: "Vietnamese",
    94: "Chinese",
}


async def get_en_msg_voice(bot_name, bot_id, message_type, input1="", input2=""):
    """英語の文章を取得."""
    bot_pronoun = await id_to_pronoun(bot_id)

    en_message = {
        "help": {
            "title": "Help",
            "url": "https://gist.github.com/AlphaIru/29971af478de6a160d94571fc581db38",
            "description": f"This is the link to {bot_name}'s manual!\n\nhttps://gist.github.com/AlphaIru/29971af478de6a160d94571fc581db38\n\n(Or click the title to the page)",
        },
        "readname_F": {
            "title": "Read Username",
            "description": f"Upon next sentences, {bot_name} will not read out each message author's username!",
        },
        "readname_T": {
            "title": "Read Username",
            "description": f"Upon next sentences, {bot_name} will read out each message author's username!",
        },
        "readbot_F": {
            "title": "Read Bot",
            "description": f"Upon next, {bot_name} will not read out each command's messages or comments!",
        },
        "readbot_T": {
            "title": "Read Bot",
            "description": f"Upon next, {bot_name} will read out each command's messages or comments!",
        },
        "mention_F": {
            "title": "Mention",
            "description": f"Upon next, {bot_name} will not read out the mentions!",
        },
        "mention_T": {
            "title": "Mention",
            "description": f"Upon next, {bot_name} will read out the mentions!",
        },
        "readotherbot_F": {
            "title": "Read Other Bots",
            "description": f"Upon next, {bot_name} will not read out other bots' messages!",
        },
        "readotherbot_T": {
            "title": "Read Other Bots",
            "description": f"Upon next, {bot_name} will read out other bots' messages!",
        },
        "deletebotmessage_F": {
            "title": "Delete Bot Messages",
            "description": f"Upon next, {bot_name} will not delete {bot_pronoun} messages!",
        },
        "deletebotmessage_T": {
            "title": "Delete Bot Messages",
            "description": f"Upon next, {bot_name} will delete {bot_pronoun} messages!",
        },
        "language": {
            "title": "Language",
            "description": f"{bot_name}'s language has been changed to English!",
        },
        "emoji_F": {
            "title": "Emoji",
            "description": f"Upon next, {bot_name} will not read out emojis!",
        },
        "emoji_T": {
            "title": "Emoji",
            "description": f"Upon next, {bot_name} will read out emojis!",
        },
        "userjoin_F": {
            "title": "User Join",
            "description": f"Upon next, {bot_name} will not read out user activities!",
        },
        "userjoin_T": {
            "title": "User Join",
            "description": f"Upon next, {bot_name} will read out user activities!",
            "em_addons": {
                0: "Join/Leave",
                1: "Guild deaf",
                2: "Guild mute",
                3: "Self deaf",
                4: "Self mute",
                5: "Screenshare",
                6: "Video/Camera stream",
            },
        },
        "blacklist": {
            "title": "Blacklist",
            "description": f"Upon next, {bot_name} will treat the added users and roles as blacklisted!",
        },
        "whitelist": {
            "title": "Whitelist",
            "description": f"Upon next, {bot_name} will treat the added users and roles as whitelisted!",
        },
        "readoutsideusers_F": {
            "title": "Non VC Users' Messages",
            "description": f"Upon next, {bot_name} will not read out users' messages who are not in the voice chat!",
        },
        "readoutsideusers_T": {
            "title": "Non VC Users' Messages",
            "description": f"Upon next, {bot_name} will read out users' messages who are not in the voice chat!",
        },
        "forcejapanese_F": {
            "title": "Force Japanese",
            "description": f"Upon next, {bot_name} will not forcefully read out messages in Japanese mode!",
        },
        "forcejapanese_T": {
            "title": "Force Japanese",
            "description": f"Upon next, {bot_name} will forcefully read out messages in Japanese mode!",
        },
        "voicedescription": {
            "title": "Voice Description",
            "description": "This will show the description of selected voice!",
            "em_addons": {
                "Voice Name": input1,
                "Voice Description": input2,
            },
        },
        "defaultvoice": {
            "title": "Default Voice",
            "description": f"{input1}'s voice settings has been changed to this default setting!",
            "em_addons": en_enumrated_voices,
        },
        "editvoice": {
            "title": f"{input1}'s Voice",
            "description": f"{input1}'s voice settings has been changed to these settings!",
            "em_addons": {
                0: "speed",
                1: "pitch",
                2: "language",
                3: "voice name",
            },
        },
        "showvoice": {
            "title": f"{input1}'s Voice",
            "description": f"{input1}'s voice settings are set in these settings!",
            "em_addons": en_enumrated_voices,
        },
        "voiceissecret": {
            "title": f"{input1}'s Voice",
            "description": f"{input1}'s voice settings are secret!",
        },
        "showsettings": {
            "title": f"{input1}'s Settings",
            "description": f"{input1}'s settings are set in these settings!",
            "em_addons": {
                0: "Read readname",
                1: f"Read {bot_name}'s Messages",
                2: "Word limit",
                3: "Read Emojis",
                4: "Read Mentions",
                5: "Read Other Bots' Messages",
                6: f"Delete {bot_name}'s Messages",
                7: f"{bot_name}'s Language",
                8: "Voicechat activity callouts",
                9: "Whitelist",
                10: "Read Non voicechat users' Messages",
                11: "Force Messages in Japanese Mode",
            },
        },
        "wordlimit": {
            "title": "Word Limit",
            "description": f"Word limit for {bot_name} has been changed to {input1}!",
        },
        "deleteallwords": {
            "title": "Delete All Words",
            "description": f"{bot_name} has deleted all words in the pronunciation dictionary!",
        },
        "resetsettings": {
            "title": "Reset Settings",
            "description": f"{bot_name}'s has resetted all settings to default!",
        },
        "addintolist": {
            "title": f"Add into the {input2}",
            "description": f"{input1} has been added into the {input2}!",
        },
        "removefromlist": {
            "title": f"Remove from the {input2}",
            "description": f"{input1} has been removed from the {input2}!",
        },
        "voicelist": {
            "title": "Voice List",
            "url": "https://gist.github.com/AlphaIru/c35ae3d62b6c99bc45ab4ec7a1e506a4",
            "description": f"This is the link to the list of voices for {bot_name}! Check out every voices for fun!\n\nhttps://gist.github.com/AlphaIru/c35ae3d62b6c99bc45ab4ec7a1e506a4",
        },
        "troubleshoot": {
            "title": "Troubleshoot",
            "description": f"These are some steps for you when {bot_name} stops reading out messages!",
            "em_addons": {
                "1": "Use `/reboot` to recall the bot again to the voicechat!",
                "2": f"Use `/addchannel` to add a message channel for {bot_name} to read out!",
                "3": f"Use `/forcebye` to force {bot_name} to leave the voicechat and use `/hello` to recall the bot again!",
                "If those did not work...": "State this issue in the Dolphin-TTS server!\n[Tip: State the condition and the method for this gltich would be very helpful to resolve the issue!`",
                "Note": "The bot maybe having trouble handling many messages at once, so please be patient!",
            },
        },
        "oldhello": {
            "title": "Hello",
            "description": f"We are very sorry, but {bot_name} will not be able to use regular commands anymore!\nPlease use `/hello` for now on!",
            "em_addons": {
                "**Invite links**": "For able to use slash commands, it might require to reinvite the bot again! Please click the links below to recall the bot!",
                "**Iru**": r"https://discord.com/api/oauth2/authorize?client_id=813401103270019102&permissions=36826448&scope=bot%20applications.commands",
                # "**Ruka**": r"https://discord.com/api/oauth2/authorize?client_id=820128974176649266&permissions=36826448&scope=bot%20applications.commands",
                # "**Dolun**": r"https://discord.com/api/oauth2/authorize?client_id=906641565441736744&permissions=36826448&scope=bot%20applications.commands",
                # "**Finta**": r"https://discord.com/api/oauth2/authorize?client_id=906641635092332586&permissions=36826448&scope=bot%20applications.commands",
                # "**Cete**": r"https://discord.com/api/oauth2/authorize?client_id=906643085264572426&permissions=36826448&scope=bot%20applications.commands",
                "**Official Discord Server**": "https://discord.gg/PBJ6969J2S",
            },
        },
        "ping": {
            "title": "Pong",
            "description": f"This will show the time that {bot_name} recieved the command and processed it!",
            "em_addons": {
                "Latency": f"The latency time is `{input1}ms`",
                "Process": f"The process time is `{input2}ms`",
            },
        },
        "credit": {
            "title": "Credit",
            "description": f"These are the people who are involved with creations of {bot_name}! Please thank them first!",
            "em_addons": {
                "Message from the Dev": " Thank you for finding this secret command! I cannot keep it up on how many people are required to create this. I do have many respects and sincere thoughts to these people, but I do have appriciations for every users who are using this right now! I will keep working on developing on this bot! Thank you for reading this! I hope you enjoy it! :heart:",
                "Dolphin-TTS Guardian": "**・Airun**",
                "Dolphin-TTS Engine/Core": "**・**TogeRaz \n**・**Tom_XV \n**・**Baku_reshi\n**・**Yuki_Trans \n**・Alpha_Iru**",
                "Special Thanks": "**・**Kazu220_ps \n**・**Wilco \n**・**Sunnyong \n**・**Jun (Lyreon) \n**・TheCorgiDoggo** \n**・**Nemy_zz \n**・**Yhay81 \n**・**cod",
                "Early Alpha Testers/Servers": "**・**アモングアス鯖(ポケモン勢): owned by Shaurufu \n**・**[Corn's Keyboard Mashers](https://discord.gg/mv8umv5brA): owned by TheCorgiDoggo \n**・**とあるオタクの緊急会議: owned by 1nRqnsh11n \n**・**Latios's Skybase: owned by Jun \n**・**[せかんど☆えでん](https://discord.gg/53G8RcqH4S): owned by Tera_Katzen \n**・**[げーみんぐ](https://discord.gg/nuBhDrN2xh): owned by yuureighost",
                "Open_JTalk (Japanese TTS)": "**・**Keiichi Tokuda \n**・**Keiichiro Oura \n**・**Kei Hashimoto \n**・**Sayaka Shiota \n**・**Shinji Takaki \n**・**Heiga Zen \n**・**Junichi Yamagishi \n**・**Tomoki Toda \n**・**Takashi Nose \n**・**Shinji Sako \n**・**Alan W. Black \n**・**Some Graduate Students from Nagoya Institute of Technology Department of Computer Science \n ",
                "Mei声": "**・**Keiichi Tokuda \n**・**Akinobu Lee \n**・**Keiichiro Oura \n**・**Daisuke Yamamoto",
                "Tohoku声": "Tohoku University Graduate School of Engineering Department of Communication Engineering Ito/Nose Laboratory",
                "Flite (English TTS)": "**・**Alan W. Black \n**・**Kevin A. Lenzo \n**・**Carnegie Mellon University \n**・**University of Edinburgh",
                "Alkana (Romaji Engine)": "**・**Cod",
                "Bep-Eng.dic (Romaji Dic)": "**・**M.Ohtsuka(mash)",
                f"{bot_name}'s picture": "**・**Alpha_Iru \n**・**Kam",
                "Terms of Usage and License": "**・**[Flite](https://github.com/festvox/flite/blob/master/COPYING) \n**・**[Open_JTalk](http://open-jtalk.sourceforge.net/readme_open_jtalk.php) \n**・**[MMDAgent](https://mmdagent-ex.dev/ja/docs/term/termofservice) \n**・**[Tohoku_Voice](https://github.com/icn-lab/htsvoice-tohoku-f01/blob/master/COPYRIGHT.txt)",
            },
        },
        "hello": {
            "title": "Hello",
            "description": f"{bot_name} has joined into the voice channel! They will start reading the messages!",
            "em_addons": {
                "**Bot Link**": "For the bot link, please use: ``/bot_discord_link``!",
                "**Official Discord Server**": "https://discord.gg/PBJ6969J2S",
            },
        },
        "byenow": {
            "title": "Bye",
            "description": f"{bot_name} has left the voice channel! Thank you for using {bot_name}!",
            "em_addons": {
                "Official Discord Server": "https://discord.gg/PBJ6969J2S",
            },
        },
        "byelater": {
            "title": "Bye",
            "description": f"{bot_name} will leave the voice channel until {bot_name} reads out all messages! Thank you for using {bot_name}!",
            "em_addons": {
                "Official Discord Server": "https://discord.gg/PBJ6969J2S",
            },
        },
        "forcedisconnect": {
            "title": "Force Disconnect",
            "description": f"{bot_name} has forcefully disconnected from the voice channel!",
        },
        "stop": {
            "title": "Stop",
            "description": f"{bot_name} has stopped reading the messages!",
        },
        "pause": {
            "title": "Pause",
            "description": f"{bot_name} has paused reading the messages!",
        },
        "resume": {
            "title": "Resume",
            "description": f"{bot_name} has resumed reading the messages!",
        },
        "reboot": {
            "title": "Reboot",
            "description": f"{bot_name} has rebooted!",
        },
        "move": {
            "title": "Move",
            "description": f"{bot_name} has moved to {input1}!",
        },
        "send": {
            "title": "Send",
            "description": f"{bot_name} has moved to {input1}!",
        },
        "addword": {
            "title": "Add Word",
            "description": f"{bot_name} has added {input1} into the pronunciation dictionary as {input2}!",
            "em_addons": {
                "Length Warning": f"The length of the word is over 50 characters, so {bot_name} has only added the first part of the words.",
            },
        },
        "reword": {
            "title": "Add Word",
            "description": f"{bot_name} has changed {input1}'s pronunciation in the pronunciation dictionary as {input2}!",
            "em_addons": {
                "Length Warning": f"The length of the word is over 50 characters, so {bot_name} has only added the first part of the words.",
            },
        },
        "importfile": {
            "title": "Import",
            "description": f"From that file, {bot_name} has added {input1} words into the pronunciation dictionary!",
            "em_addons": {
                0: {"Warning": "-------------------------------------\n"},
                1: {
                    "**・Duplicates (Outside the file)**": "There were duplicated words inbetween the imported file and the pronunciation dictionary, so the pronunciation from the file has been overwritten onto the pronunciation dictionary!",
                },
                2: {
                    "**・Duplicates (Inside the file)**": "There were duplicated words in the imported file, so the pronuncation closer to start of the file are prioritized to be saved!",
                },
                3: {
                    "**・Duplicates (Inside)**": "Some of the imported words and its pronunciation were same, so those words are not added!",
                },
                4: {
                    "**・Length of the word**": "Some words were too long to be added, so the part of the end of word might been cut off!",
                },
                5: {
                    "**・No Pronuncition**": "There were some words without a pronunciation in the file, so those words are not added!",
                },
                6: {
                    "**・Number of the words in dictionary**": "There were too many words in the pronunciation dictionary already; the words closer to the start of the file has been prioritized to be saved!",
                },
                7: {
                    "**・Type Error**": "Some of the words in the file were not in string format,so those words are not added!",
                },
            },
        },
        "exportfile": {
            "title": "Export",
            "description": f"{bot_name} has exported the pronunciation dictionary into the file!",
            "em_addons": {
                "File Info": f"Extension of this file is `{input1}`, and the file size is `{input2} Bytes` !",
            },
        },
        "deleteword": {
            "title": "Delete Word",
            "description": f"{bot_name} has deleted {input1} from the pronunciation dictionary!",
        },
        "botdiscordlink": {
            "title": "Bot Discord Link",
            "url": "https://discord.gg/PBJ6969J2S",
            "description": f"These are the links to call us and the link to {bot_name}'s official Discord server!",
            "em_addons": {
                "**Iru**": r"https://discord.com/api/oauth2/authorize?client_id=813401103270019102&permissions=36826448&scope=bot%20applications.commands",
                # "**Ruka**": r"https://discord.com/api/oauth2/authorize?client_id=820128974176649266&permissions=36826448&scope=bot%20applications.commands",
                # "**Dolun**": r"https://discord.com/api/oauth2/authorize?client_id=906641565441736744&permissions=36826448&scope=bot%20applications.commands",
                # "**Finta**": r"https://discord.com/api/oauth2/authorize?client_id=906641635092332586&permissions=36826448&scope=bot%20applications.commands",
                # "**Cete**": r"https://discord.com/api/oauth2/authorize?client_id=906643085264572426&permissions=36826448&scope=bot%20applications.commands",
                "**Official Discord Server**": "https://discord.gg/PBJ6969J2S",
            },
        },
        "addchannel": {
            "title": "Add Channel",
            "description": f"Upon next, {bot_name} will read messages from {input1}!",
            "em_addons": {
                "List of channels to read out: ": input2,
            },
        },
        "byechannel": {
            "title": "Bye",
            "description": f"{bot_name} has left the voice channel due to lack of channels to read out! Thank you for using {bot_name}!",
        },
        "removechannel": {
            "title": "Remove Channel",
            "description": f"{bot_name} will no longer read messages from {input1}!",
            "em_addons": {
                "List of channels to read out: ": input2,
            },
        },
        "botmention": {
            "title": {bot_name},
            "description": f"{bot_name}'s help commands are [/help]!",
        },
        "byevoicesingle": {
            "title": "Bye",
            "description": f"{bot_name} has left the voice channel due to lack of people in the voicechat! Thank you for using {bot_name}!",
        },
        "byevoicebot": {
            "title": "Bye",
            "description": f"{bot_name} has left the voice channel due to lack of actual people in the voicechat! Thank you for using {bot_name}!",
        },
        "byeforce": {
            "title": "Bye",
            "description": f"{bot_name} has recieved the force disconnect command! It can cause stability issues, so please refrain from doing this procedure. Thank you for using {bot_name}!",
        },
        "byeafk": {
            "title": "Bye",
            "description": f"{bot_name} has left the voice channel due to being AFK in the voice chat! Thank you for using {bot_name}!",
        },
        # -------------------------
        "missingvoice": {
            "title": "Error",
            "description": f"{bot_name} can't find the voice that you have selected!",
        },
        "nowordsindictionary": {
            "title": "Error",
            "description": f"{bot_name} didn't find any words in the pronunciation dictionary!",
        },
        "toomuchinlist": {
            "title": "Error",
            "description": f"{bot_name} cannot add {input1} into {input2} because {input2} is full already! Please delete some off from the list!",
        },
        "repeatinlist": {
            "title": "Error",
            "description": f"{bot_name} cannot add {input1} into {input2} because {input1} is already in the list!",
        },
        "notinlist": {
            "title": "Error",
            "description": f"{bot_name} cannot remove {input1} from {input2} because {input1} is not in the list!",
        },
        "usernotconnected": {
            "title": "Error",
            "description": "You are not connnected to the voice chat!",
        },
        "alreadyconnected": {
            "title": "Error",
            "description": f"{bot_name} is already connected to the voice chat!",
        },
        "otherdolphinconnected": {
            "title": "Error",
            "description": "Other dolphin is already connected to the voice chat! Please use them!",
        },
        "fullservice": {
            "title": "Error",
            "description": f"{bot_name} is running at full service right now! Please try again later!",
        },
        "toomanymembers": {
            "title": "Error",
            "description": "The number of the members in this voice channel is on limits right now, please try again later!",
        },
        "notfinishedreading": {
            "title": "Error",
            "description": f"{bot_name} is still reading out sentences! Please try again after {bot_name} finishes reading out!",
        },
        "notenoughpermission": {
            "title": "Error",
            "description": f"{bot_name} does not have any permission to be in this voice channel!\n\nAsk the admins to give [view channels], [connect], and [speak] to {bot_name}!",
        },
        "notconnected": {
            "title": "Error",
            "description": f"{bot_name} is not connected to the voice channel!",
        },
        "notreading": {
            "title": "Error",
            "description": f"Currently, {bot_name} is not reading out sentences!",
        },
        "alreadypaused": {
            "title": "Error",
            "description": f"{bot_name} is already paused!",
        },
        "alreadyresumed": {
            "title": "Error",
            "description": f"{bot_name} is already resumed!",
        },
        "notenoughmembers": {
            "title": "Error",
            "description": "There is no one in this voice channel!",
        },
        "samewords": {
            "title": "Error",
            "description": "The pronunciation and spelling of the word are same!!",
        },
        "overdic": {
            "title": "Error",
            "description": "The number of the words in the pronunciation dictionary is on limits right now, please delete some!",
        },
        "filesizetoobig": {
            "title": "Error",
            "description": "The file size is too huge! Please try again with a smaller file!",
        },
        "fileextensionerror": {
            "title": "Error",
            "description": "The file extension is not supported! Please try again with a supported file!",
            "em_addons": {
                "**Supported filename extensions:**": "`.txt` `.csv` `.dict`",
            },
        },
        "filecorrupted": {
            "title": "Error",
            "description": "The file is corrupted! Please check the format!",
        },
        "filetypeerror": {
            "title": "Error",
            "description": "The items from the file are not in string!",
        },
        "noword": {
            "title": "Error",
            "description": "There is no selected word in the pronunciation dictionary!",
        },
        "toomanychannels": {
            "title": "Error",
            "description": f"There are too many message channels to read it out! Please remove some before adding {input1}!",
        },
        "channelalreadyadded": {
            "title": "Error",
            "description": f"{input1} is already added for {bot_name} to read out!",
        },
        "channelnotadded": {
            "title": "Error",
            "description": f"{input1} is not added for {bot_name} to read out!",
        },
        "missingarguments": {
            "title": "Error",
            "description": "You are missing some arguments to use this command!",
        },
        "botmissingpermissions": {
            "title": "Error",
            "description": f"{bot_name} is missing some permissions to use this command!",
        },
        "cooldown": {
            "title": "Error",
            "description": f"That command is on cooldown! Please try again after {input1} seconds!",
        },
        "missingpermissions": {
            "title": "Error",
            "description": "You are missing some permissions to use this command!",
        },
        "userinputerror": {
            "title": "Error",
            "description": "The user input is not in the correct format! Please check the inputs again!",
        },
        "notadmin": {
            "title": "Error",
            "description": "You are not an admin!",
        },
        "inblacklist": {
            "title": "Blacklist",
            "description": "You are in the blacklist! That command will be ignored!",
        },
        "notinwhitelist": {
            "title": "Whitelist",
            "description": "You are not in the whitelist! That command will be ignored!",
        },
        "noprivateerror": {
            "title": "Error",
            "description": "You cannot use this command in the direct/private message!",
        },
        "unknownerror": {
            "title": "Error",
            "description": "Serious error just happened! Please report this bug to the pod immediately!",
            "em_addons": {
                "Name of the Error: ": type(input1).__name__,
                "Description of the Error: ": str(input1),
            },
        },
        "botbored": {
            "title": "Bored",
            "description": f"{bot_name} is bored!",
        },
    }

    en_voice_iru = {
        "help": "This is the link to the us, Yomasete Iruka, bot's manual, please check it out for here for commands!",
        "readname_F": "Upon next sentences, I will not read out the author of each messages!",
        "readname_T": "Upon next sentences, I will read out the author of each messages!",
        "readbot_F": "Upon next, I will not read out messages or comments! (I am sad...)",
        "readbot_T": "Upon next, I will read out messages or comments! (Thank you!)",
        "mention_F": "Upon next, I will not read out mentions!",
        "mention_T": "Upon next, I will read out mentions!",
        "readotherbot_F": "Upon next, I will not read out other bots' messages!",
        "readotherbot_T": "Upon next, I will read out other bots' messages!",
        "deletebotmessage_F": "Upon next, I will not delete my messages!",
        "deletebotmessage_T": "Upon next, I will delete my messages!",
        "language": "Hello! My new language is set to English!",
        "emoji_F": "Upon next, I will not read out emojis!",
        "emoji_T": "Upon next, I will read out emojis!",
        "userjoin_F": "Upon next, I will not read out user activities!",
        "userjoin_T": "Upon next, I will read out user activities!",
        "blacklist": "I will treat the added users and roles as blacklisted!",
        "whitelist": "I will treat the added users and roles as whitelisted!",
        "readoutsideusers_F": "Upon next, I will not read out users' messages who are not in the voice chat!",
        "readoutsideusers_T": "Upon next, I will read out users' messages who are not in the voice chat!",
        "forcejapanese_F": "Upon next, I will not read out messages in Japanese mode!",
        "forcejapanese_T": "Upon next, I will read out messages in Japanese mode!",
        "voicedescription": "I will show your selected voice's description!",
        "defaultvoice": f"{input1}'s voice settings has been changed to this default setting!",
        "editvoice": f"{input1}'s voice settings has been changed to these settings!",
        "showvoice": f"{input1}'s voice settings are set in these settings!",
        "voiceissecret": "My voice is secret! Sorry!",
        "showsettings": f"{input1}'s settings are set in these settings!",
        "wordlimit": f"Word limit has been changed to {input1}!",
        "deleteallwords": "I have deleted all words in the pronunciation dictionary!",
        "resetsettings": "I have resetted all settings to default!",
        "addintolist": f"{input1} has been added into the {input2}!",
        "removefromlist": f"{input1} has been removed from the {input2}!",
        "voicelist": "This is the link to the list of voices that I accepted! I suggest to check it out everything!",
        "troubleshoot": "These are some steps for you when I stop reading out the messages!",
        "oldhello": "Thank you for using me for a long time! I hope you enjoy entertaining with me!",
        "ping": f"It took {input1} milliseconds to recieve and took {input2} milliseconds to process those commands!",
        "credit": "These people helped to create me! Say thanks to everyone, and thank you from me too!",
        "hello": "Hello! I am Iru the Dolphin, and I will be reading out the messages! Best regards!",
        "byenow": "Bye! I will leave the voice channel! Thank you very much!",
        "byelater": "Bye! I will leave the voice channel! Thank you very much until the end!",
        "forcedisconnect": "I have forcefully left from the voice channel!",
        "stop": "I have stopped reading out the messages!",
        "pause": "I have paused reading out the messages!",
        "resume": "I have resumed reading out the messages!",
        "reboot": "I have rebooted myself!",
        "move": f"I have moved to {input1}!",
        "send": f"I have moved to {input1}!",
        "addword": f"{input1} has been added into the pronunciation dictionary!",
        "reword": f"{input1} has been changed in the pronunciation dictionary!",
        "importfile": f"I have imported words from {input1} into the pronunciation dictionary!",
        "exportfile": "I have exported words from the pronunciation dictionary!",
        "deleteword": f"I have deleted {input1} from the pronunciation dictionary!",
        "botdiscordlink": "This is the link to the Discord server where I am!",
        "addchannel": f"I will readout messages from {input1}!",
        "byechannel": "Thank you! I left the voice channel because there are no channels for me to read out!",
        "removechannel": f"I will not readout messages from {input1}!",
        "botmention": "My help commands are: [fowardslash help]!",
        "byevoicesingle": "I have left the voice channel due to lack of people in voice chat!",
        "byevoicebot": "I have left the voice channel due to lack of real people in voice chat!",
        "byeforce": "I have recieved the force disconnect command, but it can cause stability issues, so please refrain from doing this procedure! Thank you for using me!",
        "byeafk": "I have left the voice channel due to being AFK in voice chat!",
        # -----
        "missingvoice": "I can't find the voice that you have selected!",
        "nowordsindictionary": "I didn't find any words in the pronunciation dictionary!",
        "toomuchinlist": f"I cannot add {input1} into {input2} because {input2} is full already! Please delete some off from the list!",
        "repeatinlist": f"I cannot add {input1} into {input2} because {input1} is already in the list!",
        "notinlist": f"I cannot remove {input1} from {input2} because {input1} is not in the list!",
        "usernotconnected": "Someone is trying to call me!",
        "alreadyconnected": "I am already connected to the voice chat!",
        "otherdolphinconnected": "My friend is already connected to the voice chat! Please use them!",
        "fullservice": "I am running at full service right now! Please try again later!",
        "toomanymembers": "There are too many members in this voice channel right now, please try again later!",
        "notfinishedreading": "I am still reading out sentences! Please try again after I finish reading out!",
        "notenoughpermission": "I do not have any permission to be in this voice channel!\n\nAsk the admins to give [view channels], [connect], and [speak] to me!",
        "notconnected": "I am not connected to the voice channel!",
        "notreading": "I am not reading out sentences right now!",
        "alreadypaused": "I am already paused!",
        "alreadyresumed": "I am already resumed!",
        "notenoughmembers": "There is no one in this voice channel!",
        "samewords": "I cannot add this word because the pronunciation and spelling of the word are same!",
        "overdic": "The number of the words in the pronunciation dictionary is on limits right now, please delete some!",
        "filesizetoobig": "The file that you have selected is too big! Please select a file with smaller file size!",
        "fileextensionerror": "That file extension is not supported! Please select a file with different extension!",
        "filecorrupted": "The file is corrupted! Please check the format!",
        "filetypeerror": "The items from the file are not in string!",
        "noword": "I cannot find the word that you have selected!",
        "toomanychannels": f"Too many message channels for me to read it out! Remove some before adding {input1}!",
        "channelalreadyadded": f"I cannot add {input1} because it is already added for me to read out!",
        "channelnotadded": f"I cannot remove {input1} because it is not added for me to read out!",
        "missingarguments": "I don't have enough arguments to use this command!",
        "botmissingpermissions": "I don't have enough permissions to use this command!",
        "cooldown": f"I am on cooldown! Use that command after {input1} seconds later!",
        "missingpermissions": "You don't have enough permissions to use this command!",
        "userinputerror": "Your inputs are not in correct format! Check it again!",
        "notadmin": "You are not an admin!",
        "inblacklist": "You are in the blacklist!",
        "notinwhitelist": "You are not in the whitelist!",
        "noprivateerror": "You cannot use this command in direct message!",
        "unknownerror": "Please report the bug immediately!",
        "botbored": "I am bored!",
    }

    en_voice_ruka = {
        "help": "Th, This is, is, the, li, link, to, to, the, do, documents, fo, for, Yo, Yoma, Yomasete, I, Iruka's, ma, manual! P, Please, ch, check, it, it, out!",
        "readname_F": "Upo, Upon, ne, next, sen, sentences, I, I, wi, will, no, not, re, read, out, out the, the, au,author, of, of, each, mee, messages!",
        "readname_T": "Upo, Upon, ne, next, sen, sentences, I, I, wi, will, re, read, out, out the, the, au, author, of, of, each, mee, messages!",
        "readbot_F": "Upo, Upon, ne, next, I, I, wi, will, no, not, re, read, out, out m, my, mee, messages! (Oh god, thank you...)",
        "readbot_T": "Upo, Upon, ne, next, I, I, wi, will, re, read, out, out m, my, mee, messages! (N, nice, to, to, meet, you, you!)",
        "mention_F": "Upo, Upon, ne, next, I, I, wi, will, no, not, re, read, out, out, mee, mentions!",
        "mention_T": "Upo, Upon, ne, next, I, I, wi, will, re, read, out, out, mee, mentions!",
        "readotherbot_F": "Upon next, I will not read out other bots' messages!",
        "readotherbot_T": "Upon next, I will read out other bots' messages!",
        "deletebotmessage_F": "Upon next, I will not delete my messages!",
        "deletebotmessage_T": "Upon next, I will delete my messages!",
        "language": "Hello! My new language is set to English!",
        "emoji_F": "Upon next, I will not read out emojis!",
        "emoji_T": "Upon next, I will read out emojis!",
        "userjoin_F": "Upon next, I will not read out user activities!",
        "userjoin_T": "Upon next, I will read out user activities!",
        "blacklist": "I will treat the added users and roles as blacklisted!",
        "whitelist": "I will treat the added users and roles as whitelisted!",
        "readoutsideusers_F": "Upon next, I will not read out users' messages who are not in the voice chat!",
        "readoutsideusers_T": "Upon next, I will read out users' messages who are not in the voice chat!",
        "forcejapanese_F": "Upon next, I will not read out messages in Japanese mode!",
        "forcejapanese_T": "Upon next, I will read out messages in Japanese mode!",
        "voicedescription": "I will show your selected voice's description!",
        "defaultvoice": f"{input1}'s voice settings has been changed to this default setting!",
        "editvoice": f"{input1}'s voice settings has been changed to these settings!",
        "showvoice": f"{input1}'s voice settings are set in these settings!",
        "voiceissecret": "My voice is secret! Sorry!",
        "showsettings": f"{input1}'s settings are set in these settings!",
        "wordlimit": f"Word limit has been changed to {input1}!",
        "deleteallwords": "I have deleted all words in the pronunciation dictionary!",
        "resetsettings": "I have resetted all settings to default!",
        "addintolist": f"{input1} has been added into the {input2}!",
        "removefromlist": f"{input1} has been removed from the {input2}!",
        "voicelist": "This is the link to the list of voices that I accepted! I suggest to check it out everything!",
        "troubleshoot": "These are some steps for you when I stop reading out the messages!",
        "oldhello": "Thank you for using me for a long time! I hope you enjoy entertaining with me!",
        "ping": f"It took {input1} milliseconds to recieve and took {input2} milliseconds to process those commands!",
        "credit": "These people helped to create me! Say thanks to everyone, and thank you from me too!",
        "hello": "Hello! I am Iru the Dolphin, and I will be reading out the messages! Best regards!",
        "byenow": "Bye! I will leave the voice channel! Thank you very much!",
        "byelater": "Bye! I will leave the voice channel! Thank you very much until the end!",
        "forcedisconnect": "I have forcefully left from the voice channel!",
        "stop": "I have stopped reading out the messages!",
        "pause": "I have paused reading out the messages!",
        "resume": "I have resumed reading out the messages!",
        "reboot": "I have rebooted myself!",
        "move": f"I have moved to {input1}!",
        "send": f"I have moved to {input1}!",
        "addword": f"{input1} has been added into the pronunciation dictionary!",
        "reword": f"{input1} has been changed in the pronunciation dictionary!",
        "importfile": f"I have imported words from {input1} into the pronunciation dictionary!",
        "exportfile": "I have exported words from the pronunciation dictionary!",
        "deleteword": f"I have deleted {input1} from the pronunciation dictionary!",
        "botdiscordlink": "This is the link to the Discord server where I am!",
        "addchannel": f"I will readout messages from {input1}!",
        "byechannel": "Thank you! I left the voice channel because there are no channels for me to read out!",
        "removechannel": f"I will not readout messages from {input1}!",
        "botmention": "My help commands are: [fowardslash help]!",
        "byevoicesingle": "I have left the voice channel due to lack of people in voice chat!",
        "byevoicebot": "I have left the voice channel due to lack of real people in voice chat!",
        "byeforce": "I have recieved the force disconnect command, but it can cause stability issues, so please refrain from doing this procedure! Thank you for using me!",
        "byeafk": "I have left the voice channel due to being AFK in voice chat!",
        # -----
        "missingvoice": "I can't find the voice that you have selected!",
        "nowordsindictionary": "I didn't find any words in the pronunciation dictionary!",
        "toomuchinlist": f"I cannot add {input1} into {input2} because {input2} is full already! Please delete some off from the list!",
        "repeatinlist": f"I cannot add {input1} into {input2} because {input1} is already in the list!",
        "notinlist": f"I cannot remove {input1} from {input2} because {input1} is not in the list!",
        "usernotconnected": "Someone is trying to call me!",
        "alreadyconnected": "I am already connected to the voice chat!",
        "otherdolphinconnected": "My friend is already connected to the voice chat! Please use them!",
        "fullservice": "I am running at full service right now! Please try again later!",
        "toomanymembers": "There are too many members in this voice channel right now, please try again later!",
        "notfinishedreading": "I am still reading out sentences! Please try again after I finish reading out!",
        "notenoughpermission": "I do not have any permission to be in this voice channel!\n\nAsk the admins to give [view channels], [connect], and [speak] to me!",
        "notconnected": "I am not connected to the voice channel!",
        "notreading": "I am not reading out sentences right now!",
        "alreadypaused": "I am already paused!",
        "alreadyresumed": "I am already resumed!",
        "notenoughmembers": "There is no one in this voice channel!",
        "samewords": "I cannot add this word because the pronunciation and spelling of the word are same!",
        "overdic": "The number of the words in the pronunciation dictionary is on limits right now, please delete some!",
        "filesizetoobig": "The file that you have selected is too big! Please select a file with smaller file size!",
        "fileextensionerror": "That file extension is not supported! Please select a file with different extension!",
        "filecorrupted": "The file is corrupted! Please check the format!",
        "filetypeerror": "The items from the file are not in string!",
        "noword": "I cannot find the word that you have selected!",
        "toomanychannels": f"Too many message channels for me to read it out! Remove some before adding {input1}!",
        "channelalreadyadded": f"I cannot add {input1} because it is already added for me to read out!",
        "channelnotadded": f"I cannot remove {input1} because it is not added for me to read out!",
        "missingarguments": "I don't have enough arguments to use this command!",
        "botmissingpermissions": "I don't have enough permissions to use this command!",
        "cooldown": f"I am on cooldown! Use that command after {input1} seconds later!",
        "missingpermissions": "You don't have enough permissions to use this command!",
        "userinputerror": "Your inputs are not in correct format! Check it again!",
        "notadmin": "You are not an admin!",
        "inblacklist": "You are in the blacklist!",
        "notinwhitelist": "You are not in the whitelist!",
        "noprivateerror": "You cannot use this command in direct message!",
        "unknownerror": "please report this bug immediately!",
        "botbored": "I am bored!",
    }

    en_voice_dolun = en_voice_iru
    en_voice_finta = en_voice_iru
    en_voice_cete = en_voice_iru

    async def id_to_voice(bot_id):
        try:
            if bot_id == 813401103270019102:
                return en_voice_iru[message_type]
            elif bot_id == 820128974176649266:
                return en_voice_ruka[message_type]
            elif bot_id == 906641565441736744:
                return en_voice_dolun[message_type]
            elif bot_id == 906641635092332586:
                return en_voice_finta[message_type]
            elif bot_id == 906643085264572426:
                return en_voice_cete[message_type]
            else:
                return en_voice_iru[message_type]
        except NameError:
            return en_voice_iru[message_type]

    return en_message[message_type], await id_to_voice(bot_id)


async def id_to_pronoun(bot_id) -> str:
    """代名詞を取得する."""
    if bot_id == 813401103270019102:
        return "his"
    elif bot_id == 820128974176649266:
        return "her"
    elif bot_id == 906641565441736744:
        return "his"
    elif bot_id == 906641635092332586:
        return "his"
    elif bot_id == 906643085264572426:
        return "his"
    else:
        return None


# pylint: enable=line-too-long
