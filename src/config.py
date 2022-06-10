import os
import json

import gspread
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS = json.loads(os.environ["CREDENTIALS"])
GC = gspread.service_account_from_dict(CREDENTIALS)

NECESSARILY_KWARGS_FOR_STUDENT = ["key", "points"]
DEFAULT_KEYS_FOR_STUDENT = ["du_room", "group"]


class VillageConfig():
    DORMITORY = "Du_village"

    SPREADSHEET_ID = "10AcN0Ygof1TLxuMlBXPK9m-I6vVxpqB5AulkEgw0mBc"

    DICT_WITH_PAGES_AND_ROWS_TO_PARSE = {"Мероприятия": {"range": "A2:C", "rows": {"du_room": 0, "key": 1, "points": 2}}}


class ItisRequestConfig():
    DORMITORY = ""

    SPREADSHEET_ID = "1qPCCiMbWs1EZaK3hNBHvpn86uNx8OmN7UpWSqfv6_jQ"

    DICT_WITH_PAGES_AND_ROWS_TO_PARSE = {"09.11.2021 - 31.03.2022": {"range": "A7:C",
                                                                     "rows": {"group": 0, "key": 1, "points": 2}},
                                         "04.05.2021 - 08.11.2021": {"range": "A7:C",
                                                                     "rows": {"group": 0, "key": 1, "points": 2}}}


class ConfigToWrite():
    SPREADSHEET_ID = "1N4XHyHWJ7E0fwOV2J45IC5fsphR85G2Sfq02K-4cFwA"

    SHEET_NAME = "students_points"
