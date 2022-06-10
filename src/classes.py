from config import NECESSARILY_KWARGS_FOR_STUDENT, DEFAULT_KEYS_FOR_STUDENT


class Student:
    def __init__(self, dict_with_student):
        """Class can be created only with necessarily_kwargs"""

        necessarily_kwargs = NECESSARILY_KWARGS_FOR_STUDENT
        default_keys = DEFAULT_KEYS_FOR_STUDENT

        for default_key in default_keys:
            setattr(self, default_key, "")

        for k, v in dict_with_student.items():
            setattr(self, k, v)

        for necessarily_kwarg in necessarily_kwargs:
            assert necessarily_kwarg in self.__dict__.keys()

        self.points = self.get_float_points(self.points)

    @staticmethod
    def get_float_points(points):
        return float(points.replace(",", "."))

    def add_points(self, new_points: str):
        self.points += self.get_float_points(new_points)

    def add_info_from_another_table(self, info_from_another_table: dict):
        for key, item in info_from_another_table.items():
            if key not in self.__dict__.keys() or self.__dict__[key] == "":
                setattr(self, key, item)

        self.add_points(info_from_another_table["points"])

    def __str__(self):
        return str(self.__dict__)
