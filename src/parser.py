from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from config import SCOPES, CREDENTIALS, GC, ItisRequestConfig, VillageConfig
from classes import Student


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


def new_get_points(config):
    gsheet = GC.open_by_key(config.SPREADSHEET_ID)
    for page, dict_with_rows_and_range in config.DICT_WITH_PAGES_AND_ROWS_TO_PARSE.items():

        current_page = gsheet.worksheet(page)
        lists_with_values = current_page.get(dict_with_rows_and_range["range"])

        result = []

        for list_with_value in lists_with_values:
            keys = list(dict_with_rows_and_range["rows"].keys())
            dict_with_student = {keys[i]: list_with_value[i]
                                 for i in range(len(list_with_value))}

            dict_with_student["dormitory"] = config.DORMITORY
            result.append(dict_with_student)

        yield result


def get_dict_with_students_from_configs(configs):
    list_with_students_dicts = []
    for config in configs:
        info_from_config = new_get_points(config)

        for info in info_from_config:
            list_with_students_dicts += info

    dict_with_students = {}
    print(list_with_students_dicts)
    for student_dict in list_with_students_dicts:
        if student_dict["key"] not in dict_with_students.keys():
            dict_with_students[student_dict["key"]] = Student(student_dict)
        else:
            dict_with_students[student_dict["key"]].add_info_from_another_table(student_dict)

    return dict_with_students


def write_points_into_table(credentials, dict_with_students) -> None:
    pass


def main():
    configs = [VillageConfig, ItisRequestConfig]

    dict_with_students = get_dict_with_students_from_configs(configs)

    for student in dict_with_students.values():
        print(student)


if __name__ == "__main__":
    main()
