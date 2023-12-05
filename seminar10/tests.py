from seminar10.flight import Flight


def test_flight():
    flight = Flight("0123", 456, "Cluj-Napoca", "Dubai")
    assert flight.get_code() == "0123"
    assert flight.get_duration() == 456
    assert flight.get_departure() == "Cluj-Napoca"
    assert flight.get_destination() == "Dubai"


def test_

if __name__ == '__main__':
    test_flight()
