from seminar10.flight import Flight


class Service:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def add(self, code, duration, departure, destination):
        flight = Flight(code, duration, departure, destination)
        self.__validator.validate(flight)
        self.__repo.add(flight)
