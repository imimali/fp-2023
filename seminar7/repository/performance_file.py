from seminar7.repository.performance import PerformanceRepository
from seminar7.repository.singer_file import SingerFileRepository
from seminar7.repository.concert_file import ConcertFileRepository
from seminar7.domain import Performance


class PerformanceFileRepository(PerformanceRepository):
    def __init__(
        self,
        file_name,
        singer_repo: SingerFileRepository,
        concert_repo: ConcertFileRepository,
    ):
        super().__init__()
        self.__file_name = file_name
        self.__concert_repo = concert_repo
        self.__singer_repo = singer_repo
        self.__read_from_file()

    def __read_from_file(self):
        with open(self.__file_name, "r") as f:
            for line in f:
                singer_id, concert_id = line.strip().split(",")
                singer = self.__singer_repo.find_by_id(int(singer_id))
                concert = self.__concert_repo.find_by_id(int(concert_id))
                performance = Performance(singer, concert)
                self.add(performance)
