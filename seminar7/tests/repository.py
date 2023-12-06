from seminar7.repository import SingerRepository
from seminar7.repository.concert_file import ConcertFileRepository
from seminar7.repository.singer_file import SingerFileRepository
from seminar7.repository.performance_file import PerformanceFileRepository
from seminar7.repository.exceptions import RepositoryException
from datetime import datetime
from seminar7.domain import Concert, Singer, Performance


def test_singer_repository():
    repo = SingerRepository()
    singer = Singer(1, "Eminem", "rap")
    repo.add(singer)
    assert len(repo) == 1


# todo add other test cases


def test_concert_repo_read():
    repo = ConcertFileRepository("/Users/maliimregergely/mig/seminar-fp/concerts.txt")
    assert len(repo.get_all()) == 2
    ...  # todo add other test cases


def test_concert_repo_write():
    repo = ConcertFileRepository("/Users/maliimregergely/mig/seminar-fp/concerts.txt")
    repo.write_to_file()
    date = datetime.strptime("2023-11-23", "%Y-%m-%d")
    repo.add(Concert(3, "Boom", "Madrid", date))
    repo.write_to_file()


def test_singer_file_repo_read():
    repo = SingerFileRepository("/Users/maliimregergely/mig/seminar-fp/singers.txt")
    # assert len(repo.get_all()) == 2
    ...  # TODO this needs to be fixed


def test_singer_file_repo_write():
    repo = SingerFileRepository("/Users/maliimregergely/mig/seminar-fp/singers.txt")
    repo.write_to_file()

    repo.add(Singer(1, "Boom", "Madrid"))
    repo.write_to_file()


def test_singer_find():
    repo = SingerFileRepository("/Users/maliimregergely/mig/seminar-fp/singers.txt")
    try:
        assert repo.find_by_id(123123)
        assert False
    except RepositoryException:
        pass
    assert repo.find_by_id(1) is not None


def test_performance_file_repo():
    # TODO split this into multiple tests
    singer_repo = SingerFileRepository(
        "/Users/maliimregergely/mig/seminar-fp/singers.txt"
    )
    concert_repo = ConcertFileRepository(
        "/Users/maliimregergely/mig/seminar-fp/concerts.txt"
    )

    performance_repo = PerformanceFileRepository(
        "/Users/maliimregergely/mig/seminar-fp/performances.txt",
        singer_repo,
        concert_repo,
    )
    assert len(performance_repo) == 4


if __name__ == "__main__":
    test_singer_repository()
    test_concert_repo_read()
    test_concert_repo_write()
    test_singer_file_repo_read()
    test_singer_file_repo_write()
    test_singer_find()
    test_performance_file_repo()
