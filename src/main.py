from config import ItisRequestConfig, VillageConfig, ConfigToWrite
from parser import get_dict_with_students_from_configs, write_points_into_table


def main():
    configs = [VillageConfig, ItisRequestConfig]

    dict_with_students = get_dict_with_students_from_configs(configs)

    write_points_into_table(ConfigToWrite, dict_with_students)


if __name__ == "__main__":
    main()
