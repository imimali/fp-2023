from seminar10.flight import Flight


class Service:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def add(self, code, duration, departure, destination):
        flight = Flight(code, duration, departure, destination)
        self.__validator.validate(flight)
        self.__repo.add(flight)

    def remove(self, code):
        self.__repo.remove(code)

    def filter_by_departure(self, departure):
        # return list(filter(lambda flight: flight.get_departure() == departure, self.__repo.get_all()))
        result = []
        for elem in self.__repo.get_all():
            if elem.get_departure() == departure:
                result.append(elem)
        return result

    def get_by_departure_sorted_by_destination(self, departure):
        all_by_departure = self.filter_by_departure(departure)

        def my_key(flight):
            return flight.get_destination()

        # return sorted(all_by_departure, key=lambda x: x.get_destination())
        return sorted(all_by_departure, key=my_key)
