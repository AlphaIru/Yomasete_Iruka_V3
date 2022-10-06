"""ログを作成する関数."""
# coding: utf-8

from datetime import datetime
from pytz import timezone


def make_new_log(log_data):
    """ログを作成する関数."""
    time = str(datetime.now(timezone("America/Los_Angeles")))

    with open("Yomasete_Iruka_V3/log/log.txt", mode="a", encoding="utf-8") as log_file:
        log_file.write(time + "\n" + log_data + "\n" + "\n")