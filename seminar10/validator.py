from seminar10.flight import Flight


class FlightValidator:
    def __init__(self):
        pass

    def validate(self, flight: Flight):
        if (
            len(flight.get_code()) < 3
            or len(flight.get_departure()) < 3
            or len(flight.get_destination()) < 3
        ):
            raise ValueError(
                "Code, departure or destination has less than three characters"
            )
        if flight.get_duration() < 20:
            raise ValueError("Duration less than twenty minutes")
