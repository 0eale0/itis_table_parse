from parser import get_credentials, get_points_from_du_and_itis_requests


def main():
    credentials = get_credentials()

    dict_with_points = get_points_from_du_and_itis_requests(credentials)

    for item in dict_with_points.items():
        print(item)


if __name__ == "__main__":
    main()
