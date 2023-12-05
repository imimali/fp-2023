from seminar10.flight import Flight
from seminar10.validator import FlightValidator
from seminar10.repository import Repository
from seminar10.service import Service


def test_flight():
    flight = Flight("0123", 456, "Cluj-Napoca", "Dubai")
    assert flight.get_code() == "0123"
    assert flight.get_duration() == 456
    assert flight.get_departure() == "Cluj-Napoca"
    assert flight.get_destination() == "Dubai"


def test_repository_add():
    repo = Repository("../test_flights.txt")
    repo.add(Flight("0123", 456, "Cluj-Napoca", "Dubai"))
    assert len(repo) == 4


def test_service_add():
    repo = Repository("../test_flights.txt")
    service = Service(repo, FlightValidator())
    service.add("0123", 45, "Cluj-Napoca", "Dubai")
    assert len(repo) == 4
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


if __name__ == "__main__":
    test_flight()
    test_repository_add()
    test_service_add()
