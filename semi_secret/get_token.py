"""トークンを取得するコード."""
import json


# TOKEN_DIRECTORY = "/home/ubuntu/tokens.json"  # nosec


def get_token(bot_name) -> str:
    """トークンを取得する."""
    with open("tokens.json", mode="r", encoding="utf-8") as file:
        token_dictionary = json.load(file)

    token_key = token_dictionary[bot_name]

    return token_key
