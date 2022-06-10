from config import GC
from classes import Student


def get_points_from_config(config) -> dict:
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


def get_dict_with_students_from_configs(configs: list) -> dict:
    list_with_students_dicts = []
    for config in configs:
        info_from_config = get_points_from_config(config)

        for info in info_from_config:
            list_with_students_dicts += info

    dict_with_students = {}
    for student_dict in list_with_students_dicts:
        if student_dict["key"] not in dict_with_students.keys():
            dict_with_students[student_dict["key"]] = Student(student_dict)
        else:
            dict_with_students[student_dict["key"]].add_info_from_another_table(student_dict)

    return dict_with_students


def write_points_into_table(config, dict_with_points: dict) -> None:
    lst_to_write = [[*dict_with_points[student].__dict__.values()]
                    for student in dict_with_points]

    gsheet = GC.open_by_key(config.SPREADSHEET_ID)
    wsheet = gsheet.worksheet(config.SHEET_NAME)

    write_from = "A1"
    write_to = chr(64 + len(lst_to_write[0])) + str(len(lst_to_write))

    wsheet.update(f'{write_from}:{write_to}', lst_to_write)
