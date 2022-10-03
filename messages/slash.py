"""スラッシュコマンド用の文章を取得するモジュール."""
# coding: utf-8
# pylint: disable=line-too-long
# pylama: ignore=E501


slash_messages = {
    "help": {
        "main": "Shows the link to the help page!",
    },
    "name": {
        "main": "Change the settings to read out the author's name of each messages!",
        "read_name": "Select if the dolphin should read out author's name!",
    },
    "readbot": {
        "main": "Change the settings to read out the dolphin's messages!",
        "read_bot": "Select if the dolphin should read out its messages!",
    },
    "mention": {
        "main": "Change the settings to read out the mention in the message!",
        "read_mention": "Select if the dolphin should read out the mentions!",
    },
    "readotherbot": {
        "main": "Change the settings to read out bots other than the dolphin's messages!",
        "read_other_bot": (
            "Select if the dolphin should read out bots other than its messages!"
        ),
    },
    "deletebotmessages": {
        "main": "Change the settings to delete the dolphin's messages after certain amounts of time!",
        "delete_bot_messages": "Select if the dolphin should delete its messages after certain amounts of time!",
    },
    "language": {
        "main": "This changes the the dolphin's language!",
        "lang": "Select the language for the dolphin!",
    },
    "emoji": {
        "main": "Change the settings to read out the emojis in the message!",
        "read_emoji": "Select if the dolphin should read out the emojis!",
    },
    "userjoin": {
        "main": "Change the settings to read out the activities in the voice chat!",
        "user_join": "Select if the dolphin should read out the activities of each users!",
        "join_leave": "Select if the dolphin should read out each users joining in and leaving out of the voicechat!",
        "guild_dea": "Select if the dolphin should read out each users being guild_deafen or not!",
        "guild_mute": "Select if the dolphin should read out each users being guild_muted or not!",
        "self_dea": "Select if the dolphin should read out each users are deafening themselves or not!",
        "self_mute": "Select if the dolphin should read out each users are muting themselves or not!",
        "self_stream": "Select if the dolphin should read out each users are streaming or not!",
        "self_video": "Select if the dolphin should read out each users are video streaming or not!",
    },
    "switchblacklist": {
        "main": "This settings will change between blacklist and whitelist!",
        "switch_blacklist": "Select if the dolphin should treat the list as the blacklist or whitelist!",
    },
    "readnonvcusers": {
        "main": "Change the settings to read out the non-VC users' messages!",
        "read_non_vc_users_message": "Select if the dolphin should read out the non-VC users' messages!",
    },
    "forcejapanese": {
        "main": "Change the settings to read out the messages in Japanese mode only!",
        "force_japanese_mode": "Select if the dolphin should read out the messages in Japanese mode only!",
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
        "main": "Changes the limit that the dolphin should read out the messages!",
        "limit": "Select the limit that the dolphin should read out the messages!",
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
        "main": "This will list out all of the available voices for the dolphin!",
    },
    "troubleshoot": {
        "main": "This will show the methods when the bot stops working!",
    },
    "ping": {
        "main": "This will show the process time and latency time of the dolphin!",
    },
    "hello": {
        "main": "This will call the dolphin to the voice chat!",
    },
    "bye": {
        "main": "This will leave the dolphin from the voice chat!",
    },
    "forcebye": {
        "main": "This will forcefully leave the dolphin from the voice chat, even if the dolphin is not in the voice chat!",
    },
    "forcelanguage": {
        "main": "This will force the dolphin to read out the message in selected language only!",
        "voice_lang": "Select the language for the message to be read out!",
        "message": "Input the message you want to read out!",
    },
    "stop": {
        "main": "This will stop the dolphin from reading out the messages!",
    },
    "pause": {
        "main": "This will pause the dolphin from reading out the messages!",
    },
    "resume": {
        "main": "This will resume the dolphin from reading out the messages!",
    },
    "clear": {
        "main": "This will clear the queues, disconnect and recall the dolphin to the voice chat!",
    },
    "send": {
        "main": "This will send the dolphin to the selected channel!",
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
        "main": "This will show the link to the dolphin's Discord server!",
    },
    "addchannel": {
        "main": "This will make the dolphin to read out the selected channel!",
        "channel": "Select the channel, which one you want the dolphin to read out!",
    },
    "removechannel": {
        "main": "This will make the dolphin not to read out the selected channel!",
        "channel": "Select the channel, which one you want the dolphin not to read out!",
    },
}
