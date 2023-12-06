from seminar10.flight import Flight
from seminar10.validator import FlightValidator
from seminar10.repository import Repository, RepositoryError
from seminar10.service import Service


def test_flight():
    flight = Flight("0123", 456, "Cluj-Napoca", "Dubai")
    assert flight.get_code() == "0123"
    assert flight.get_duration() == 456
    assert flight.get_departure() == "Cluj-Napoca"
    assert flight.get_destination() == "Dubai"


def test_repository_add():
    repo = Repository("../test_flights.txt")
    # assert len(repo) == 1
    repo.clear()
    repo.add(Flight("0123", 456, "Cluj-Napoca", "Dubai"))
    assert len(repo) == 1


def test_service_add():
    repo = Repository("../test_flights.txt")
    repo.clear()
    service = Service(repo, FlightValidator())
    service.add("0123", 45, "Cluj-Napoca", "Dubai")
    assert len(repo) == 1
    try:
        service.add("0", 45, "Cluj-Napoca", "Dubai")
        assert False
    except ValueError:
        assert True

    try:
        service.add("0123", 45, "Cl", "Dubai")
        assert False
    except ValueError:
        assert True

    try:
        service.add("0123", 45, "Cluj", "Du")
        assert False
    except ValueError:
        assert True

    try:
        service.add("0123", 15, "Cluj", "Dubai")
        assert False
    except ValueError:
        assert True


def test_repo_find_by_code():
    repo = Repository("../test_flights.txt")
    repo.clear()
    repo.add(Flight("0123", 456, "Cluj-Napoca", "Dubai"))
    assert repo.find_by_code("0123") is not None
    assert repo.find_by_code("0123").get_destination() == "Dubai"

    try:
        repo.find_by_code("012123")
        assert False
    except RepositoryError:
        assert True


def test_repo_remove():
    repo = Repository("../test_flights.txt")
    repo.clear()
    repo.add(Flight("0123", 456, "Cluj-Napoca", "Dubai"))
    repo.remove("0123")
    assert len(repo) == 0


def test_service_remove():
    repo = Repository("../test_flights.txt")
    repo.clear()
    service = Service(repo, FlightValidator())
    service.add("0123", 45, "Cluj-Napoca", "Dubai")
    service.remove("0123")
    assert len(repo) == 0


def test_repo_get_all():
    repo = Repository("../test_flights.txt")
    repo.clear()
    flight = Flight("0123", 456, "Cluj-Napoca", "Dubai")
    repo.add(flight)
    assert repo.get_all() == [flight]


def test_repo_filter_by_departure():
    repo = Repository("../test_flights.txt")
    repo.clear()
    service = Service(repo, FlightValidator())
    service.add("0123", 45, "Cluj-Napoca", "Dubai")
    assert service.filter_by_departure("Cluj-Napoca") == [
        Flight("0123", 45, "Cluj-Napoca", "Dubai")
    ]


def test_service_get_by_departure_sorted_by_destination():
    repo = Repository("../test_flights.txt")
    repo.clear()
    service = Service(repo, FlightValidator())
    service.add("0123", 45, "Cluj-Napoca", "Dubai")
    service.add("0123", 45, "Cluj-Napoca", "Cairo")
    service.add("0123", 45, "Cluj", "Cairo")
    result = service.get_by_departure_sorted_by_destination("Cluj-Napoca")
    assert len(result) == 2
    assert result[0].get_destination() == "Cairo"
    assert result[1].get_destination() == "Dubai"


def test_repo_update():
    repo = Repository("../test_flights.txt")
    repo.clear()
    flight = Flight("0123", 456, "Cluj-Napoca", "Dubai")
    repo.add(flight)
    repo.update_duration("0123", 123)
    assert repo.find_by_code("0123").get_duration() == 123


def test_service_bulk_increase_duration_by_departure():
    repo = Repository("../test_flights.txt")
    repo.clear()
    service = Service(repo, FlightValidator())
    service.add("0123", 45, "Cluj-Napoca", "Dubai")
    service.add("0124", 55, "Cluj-Napoca", "Cairo")
    service.add("0125", 45, "Cluj", "Cairo")
    service.bulk_increase_duration_by_departure("Cluj-Napoca", 10)
    assert repo.find_by_code("0123").get_duration() == 55
    assert repo.find_by_code("0124").get_duration() == 65
    assert repo.find_by_code("0125").get_duration() == 45


if __name__ == "__main__":
    test_flight()
    test_repository_add()
    test_service_add()
    test_repo_find_by_code()
    test_repo_remove()
    test_service_remove()
    test_repo_get_all()
    test_repo_filter_by_departure()
    test_service_get_by_departure_sorted_by_destination()
    test_repo_update()
    test_service_bulk_increase_duration_by_departure()
