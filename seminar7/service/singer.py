from seminar7.repository import SingerRepository
from seminar7.domain import Singer, SingerValidator


class SingerService:
    def __init__(self):
        self.__repo = SingerRepository()
        self.__validator = SingerValidator()

    def add(self, singer_id, name, genre):
        singer = Singer(singer_id, name, genre)
        self.__validator.validate(singer)
        self.__repo.add(singer)

    def get_all(self):
        return self.__repo.get_all()

    def get_nr_singers_by_all_genres(self):
        """"""
        result = dict()
        for singer in self.get_all():
            if singer.get_genre() in result:
                result[singer.get_genre()] += 1
            else:
                result[singer.get_genre()] = 1
        return result
