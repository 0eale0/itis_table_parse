from parser import get_credentials, get_points_from_configs
from config import VillageConfig, ItisRequestConfig


def main():
    credentials = get_credentials()
    configs = [VillageConfig, ItisRequestConfig]

    dict_with_points = get_points_from_configs(credentials, configs)

    for item in dict_with_points.items():
        print(item)


if __name__ == "__main__":
    main()
