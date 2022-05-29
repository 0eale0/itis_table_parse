from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import SCOPES, CREDENTIALS, VillageConfig, ItisRequestConfig


def get_credentials():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config(CREDENTIALS, SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    return credentials


def get_points(credentials, dict_with_points, spreadsheet_id, range_name, rows_to_parse, dormitory=""):
    try:
        service = build("sheets", "v4", credentials=credentials)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get("values", [])

        row_for_name = rows_to_parse["key"]
        row_for_points = rows_to_parse["item"]

        print(values)

        for row in values:
            name = row[row_for_name]
            points = float(row[row_for_points].replace(",", "."))

            if name:
                if name not in dict_with_points.keys():
                    dict_with_points[name] = {"points": 0, "dormitory": ""}

                dict_with_points[name]["points"] += points

                if dormitory:
                    dict_with_points[name]["dormitory"] = dormitory

        return dict_with_points
    except HttpError as err:
        print(err)
        return err


def get_points_from_configs(credentials, configs: list) -> dict:
    dict_with_points = {}

    for config in configs:
        spreadsheet_id = config.SPREADSHEET_ID
        dict_with_ranges_and_rows_to_parse = config.DICT_WITH_RANGES_AND_ROWS_TO_PARSE
        dormitory = config.DORMITORY

        for range_name in dict_with_ranges_and_rows_to_parse.keys():
            rows_to_parse = dict_with_ranges_and_rows_to_parse[range_name]

            dict_with_points = get_points(credentials, dict_with_points, spreadsheet_id,
                                          range_name, rows_to_parse, dormitory)

    sorted_dict_with_points = {k: v for k, v in sorted(dict_with_points.items(),
                                                       key=lambda item: item[1]["points"], reverse=True)}
    return sorted_dict_with_points


def write_points_into_table(credentials) -> None:
    pass


def main():
    pass


if __name__ == "__main__":
    main()
