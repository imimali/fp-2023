from seminar10.flight import Flight


class RepositoryError(Exception):
    pass


class Repository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__elements = []
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__file_name, "r") as f:
                for line in f:
                    code, duration, departure, destination = line.strip().split(",")
                    self.__elements.append(
                        Flight(code, duration, departure, destination)
                    )
        except FileNotFoundError as nf:
            raise RepositoryError(nf)

    def add(self, element):
        self.__elements.append(element)

    def __len__(self):
        return len(self.__elements)
