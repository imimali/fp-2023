from .singer import Singer


class ValidatorException(Exception):
    pass


class SingerValidator:
    def __init__(self):
        self.__accepted_genres = ["rap", "rock", "pop"]

    def validate(self, singer: Singer):
        errors = []
        if len(singer.get_name()) < 6:
            errors.append("Name must have at least 6 characters")

        if singer.get_genre() not in self.__accepted_genres:
            errors.append(f"Genre must be one of {self.__accepted_genres}")

        if errors:
            raise ValidatorException(", ".join(errors))
