import os
import json

from dotenv import load_dotenv

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
CREDENTIALS = json.loads(os.environ["CREDENTIALS"])


class VillageConfig:
    DORMITORY = "Du_village"

    SPREADSHEET_ID = "10AcN0Ygof1TLxuMlBXPK9m-I6vVxpqB5AulkEgw0mBc"

    DICT_WITH_RANGES_AND_ROWS_TO_PARSE = {"Мероприятия!B2:E": {"key": 0, "item": 1}}


class ItisRequestConfig:
    DORMITORY = ""

    SPREADSHEET_ID = "1qPCCiMbWs1EZaK3hNBHvpn86uNx8OmN7UpWSqfv6_jQ"

    DICT_WITH_RANGES_AND_ROWS_TO_PARSE = {"09.11.2021 - 31.03.2022!B7:C": {"key": 0, "item": 1},
                                          "04.05.2021 - 08.11.2021!B7:C": {"key": 0, "item": 1}}
