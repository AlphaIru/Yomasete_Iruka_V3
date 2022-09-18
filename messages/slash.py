"""スラッシュコマンド用の文章を取得するモジュール."""
# coding: utf-8
# pylint: disable=line-too-long
# pylama: ignore=E501


def get_slash_messages(command_type, search_msg, name_en=None, pronoun_en=None):
    """スラッシュコマンド用の文章を取得する関数."""
    slash_messages = {
        "help": {
            "main": "Shows the link to the help page!",
        },
        "name": {
            "main": "Change the settings to read out the author's name of each messages!",
            "read_name": f"Select if {name_en} should read out author's name!",
        },
        "readbot": {
            "main": f"Change the settings to read out {name_en}'s messages!",
            "read_bot": f"Select if {name_en} should read out {pronoun_en} messages!",
        },
        "mention": {
            "main": "Change the settings to read out the mention in the message!",
            "read_mention": f"Select if {name_en} should read out the mentions!",
        },
        "readotherbot": {
            "main": f"Change the settings to read out bots other than {name_en}'s messages!",
            "read_other_bot": (
                f"Select if {name_en} should read out bots other than {pronoun_en} messages!"
            ),
        },
        "deletebotmessages": {
            "main": f"Change the settings to delete {name_en}'s messages after certain amounts of time!",
            "delete_bot_messages": f"Select if {name_en} should delete {pronoun_en} messages after certain amounts of time!",
        },
        "language": {
            "main": f"This changes the {name_en}'s language!",
            "lang": f"Select the language for {name_en}!",
        },
        "emoji": {
            "main": "Change the settings to read out the emojis in the message!",
            "read_emoji": f"Select if {name_en} should read out the emojis!",
        },
        "userjoin": {
            "main": "Change the settings to read out the activities in the voice chat!",
            "user_join": f"Select if {name_en} should read out the activities of each users!",
            "join_leave": f"Select if {name_en} should read out each users joining in and leaving out of the voicechat!",
            "guild_deaf": f"Select if {name_en} should read out each users being guild_deafen or not!",
            "guild_mute": f"Select if {name_en} should read out each users being guild_muted or not!",
            "self_deaf": f"Select if {name_en} should read out each users are deafening themselves or not!",
            "self_mute": f"Select if {name_en} should read out each users are muting themselves or not!",
            "self_stream": f"Select if {name_en} should read out each users are streaming or not!",
            "self_video": f"Select if {name_en} should read out each users are video streaming or not!",
        },
        "switchblacklist": {
            "main": "This settings will change between blacklist and whitelist!",
            "switch_blacklist": f"Select if {name_en} should treat the list as the blacklist or whitelist!",
        },
        "readnonvcusers": {
            "main": "Change the settings to read out the non-VC users' messages!",
            "read_non_vc_users_message": f"Select if {name_en} should read out the non-VC users' messages!",
        },
        "forcejapanese": {
            "main": "Change the settings to read out the messages in Japanese mode only!",
            "force_japanese_mode": f"Select if {name_en} should read out the messages in Japanese mode only!",
        },
        "voicedescription": {
            "main": "This will show the description of the selected voice!",
            "voice_lang": "Select the language of the voice!",
            "select_voice": "Select the voice you want to see the description of!",
        },
        "defaultvoice": {"main": "Set the user's default voice settings!"},
        "voice": {
            "main": "Changes the user's voices!",
            "select_speed": "Select the new voice speed!",
            "select_pitch": "Select the new voice pitch!",
            "voice_lang": "Select the language for the new voice!",
            "select_voice": "Select the new voice!",
        },
        "show": {
            "main": "Shows the current voice settings!",
            "member": "Select the member, which one you want to see their settings!",
        },
        "showsettings": {
            "main": "Shows all of the current server's settings!",
        },
        "length": {
            "main": f"Changes the limit that {name_en} should read out the messages!",
            "limit": f"Select the limit that {name_en} should read out the messages!",
        },
        "deleteallwords": {
            "main": "This will delete all words in the server's pronunciation dictionary!",
        },
        "resetsettings": {
            "main": "This will reset all settings to the default settings!",
        },
        "adduserblacklist": {
            "main": "This will add a selected member into the blacklist!",
            "member": "Select the member, which one you want to add into the blacklist!",
            "no_command": "Select if that user are not allowed to use setting related commands!",
            "no_voice": "Select if that user are not allowed to read out their messages!",
        },
        "addroleblacklist": {
            "main": "This will add a selected role into the blacklist!",
            "role": "Select the role, which one you want to add into the blacklist!",
            "no_command": "Select if that role are not allowed to use setting related commands!",
            "no_voice": "Select if that role are not allowed to read out their messages!",
        },
        "removeuserblacklist": {
            "main": "This will remove a selected member from the blacklist!",
            "member": "Select the member, which one you want to remove from the blacklist!",
        },
        "removeroleblacklist": {
            "main": "This will remove a selected role from the blacklist!",
            "role": "Select the role, which one you want to remove from the blacklist!",
        },
        "voicelist": {
            "main": f"This will list out all of the available voices for {name_en}!",
        },
        "troubleshoot": {
            "main": "This will show the methods when the bot stops working!",
        },
        "ping": {
            "main": f"This will show the process time and latency time of {name_en}!",
        },
        "hello": {
            "main": f"This will call {name_en} to the voice chat!",
        },
        "bye": {
            "main": f"This will leave {name_en} from the voice chat!",
        },
        "forcebye": {
            "main": f"This will forcefully leave {name_en} from the voice chat, even if {name_en} is not in the voice chat!",
        },
        "forcelanguage": {
            "main": f"This will force {name_en} to read out the message in selected language only!",
            "voice_lang": "Select the language for the message to be read out!",
            "message": "Input the message you want to read out!",
        },
        "stop": {
            "main": f"This will stop {name_en} from reading out the messages!",
        },
        "pause": {
            "main": f"This will pause {name_en} from reading out the messages!",
        },
        "resume": {
            "main": f"This will resume {name_en} from reading out the messages!",
        },
        "clear": {
            "main": f"This will clear the queues, disconnect and recall {name_en} to the voice chat!",
        },
        "send": {
            "main": f"This will send {name_en} to the selected channel!",
        },
        "addword": {
            "main": "This will add a word into the server's pronunciation dictionary!",
            "word1": "Type the word, which one you want to add into the dictionary!",
            "word2": "Type the for the word!",
        },
        "importfile": {
            "main": "This will import the list of words into pronunciation dictionary from the file!",
            "attachment": "Select the file (.txt, .csv, .dic, .dict, .json), which one you want to import!",
        },
        "exportfile": {
            "main": "This will export the list of words from the pronunciation dictionary as a file!",
            "mode": "Select the file format, which one you want to export! (.dict is in UTF-16)",
        },
        "deleteword": {
            "main": "This will delete a word from the server's pronunciation dictionary!",
            "word": "Type the word, which one you want to delete from the dictionary!",
        },
        "botdiscordlink": {
            "main": f"This will show the link to {name_en}'s Discord server!",
        },
        "addchannel": {
            "main": f"This will make {name_en} to read out the selected channel!",
            "channel": f"Select the channel, which one you want {name_en} to read out!",
        },
        "removechannel": {
            "main": f"This will make {name_en} not to read out the selected channel!",
            "channel": f"Select the channel, which one you want {name_en} not to read out!",
        },
    }

    return slash_messages[command_type][search_msg]
