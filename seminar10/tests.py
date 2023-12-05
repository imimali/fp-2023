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
    assert len(repo) == 1
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


if __name__ == "__main__":
    test_flight()
    test_repository_add()
    test_service_add()
    test_repo_find_by_code()
    test_repo_remove()
    test_service_remove()
