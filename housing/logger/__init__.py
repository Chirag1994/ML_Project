import os
import logging
import pandas as pd
from datetime import datetime
from housing.constant import get_current_time_stamp

LOG_DIR = "logs"


def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"


LOG_FILE_NAME = get_log_file_name()

os.makedirs(LOG_FILE_NAME, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="w",
    format="[%(asctime)s]^; %(levelname)s^; %(filename)s^; %(funcName)s^; %(message)s",
    level=logging.INFO,
)


def get_log_dataframe(filepath):
    data = []
    with open(filepath) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))
    log_df = pd.DataFrame(data)
    columns = [
        "Time Stamp",
        "Log Level",
        "Line Number",
        "File Name",
        "Function Name",
        "Message",
    ]
    log_df.columns = columns
    log_df["Log_Message"] = log_df["Time Stamp"].astype(str) + ":$" + log_df["Message"]
    return log_df[["Log_Message"]]
