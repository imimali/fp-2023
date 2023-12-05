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

    def __write_to_file(self):
        try:
            with open(self.__file_name, "w") as f:
                for element in self.__elements:
                    flight_string = f"{element.get_code()},{element.get_duration()},{element.get_departure()},{element.get_destination()}"
                    f.write(flight_string + "\n")
        except FileNotFoundError as nf:
            raise RepositoryError(nf)

    def clear(self):
        self.__elements = []
        self.__write_to_file()

    def add(self, element):
        self.__elements.append(element)
        self.__write_to_file()

    def remove(self, code):
        flight = self.find_by_code(code)
        self.__elements.remove(flight)
        self.__write_to_file()

    def find_by_code(self, code):
        for elem in self.__elements:
            if elem.get_code() == code:
                return elem
        raise RepositoryError(f"Elem with code {code} not found")

    def __len__(self):
        return len(self.__elements)
