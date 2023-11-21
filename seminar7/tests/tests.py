from seminar7.domain import Singer, ValidatorException
from seminar7.repository import SingerRepository
from seminar7.service import SingerService


def test_singer():
    singer = Singer(1, "Eminem", "rap")
    assert singer.get_name() == "Eminem"
    assert singer.get_id() == 1
    assert singer.get_genre() == "rap"
    assert str(singer) == "Singer(id=1,name=Eminem,genre=rap)"

    assert singer != Singer(2, "Eminem", "rap")
    assert singer == Singer(1, "Eminem", "rap")


def test_repository():
    repo = SingerRepository()
    singer = Singer(1, "Eminem", "rap")
    repo.add(singer)
    assert len(repo) == 1


def test_service():
    service = SingerService()

    try:
        service.add(1, "a", "werewr")
        # assert False,"Should never get here"
        raise AssertionError("Should never get here")
    except ValidatorException as ve:
        assert (
            str(ve)
            == "Name must have at least 6 characters, Genre must be one of ['rap', 'rock', 'pop']"
        )

    service.add(1, "Eminem", "rap")
    assert len(service.get_all()) == 1


def test_servive_genre_report():
    service = SingerService()
    assert service.get_nr_singers_by_all_genres() == {}
    service.add(1, "Eminem", "rap")

    assert service.get_nr_singers_by_all_genres() == {"rap": 1}

    service.add(2, "Tupac Shakur", "rap")
    assert service.get_nr_singers_by_all_genres() == {"rap": 2}
    service.add(3, "Smiley", "pop")
    assert service.get_nr_singers_by_all_genres() == {"rap": 2, "pop": 1}
    service.add(4, "Ozzy Osbourne", "rock")
    assert service.get_nr_singers_by_all_genres() == {"rap": 2, "pop": 1, "rock": 1}


if __name__ == "__main__":
    test_singer()
    test_repository()
    test_service()
    test_servive_genre_report()
