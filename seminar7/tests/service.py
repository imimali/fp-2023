from seminar7.domain import ValidatorException
from seminar7.service import SingerService


def test_singer_service():
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


def test_performance_service_genre_report():
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
    test_singer_service()
    test_performance_service_genre_report()
