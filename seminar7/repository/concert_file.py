from datetime import datetime
from seminar7.domain import Concert


class RepositoryException(Exception):
    pass


class ConcertFileRepository:
    def __init__(self, file_name: str):
        self.__elements = []
        self.__file_name = file_name
        self.__read_concerts()

    def __read_concerts(self):
        """
        Read concerts from file
        :return:
        """
        file = None
        try:
            # we use the old open & close mechanism
            file = open(self.__file_name, "r")
            while line := file.readline():
                components = line.strip().split(",")
                concert_id = int(components[0])
                name = components[1]
                location = components[2]
                date = datetime.strptime(components[3], "%Y-%m-%d")
                self.__elements.append(Concert(concert_id, name, location, date))

        except FileNotFoundError as fe:
            raise RepositoryException("File not found " + str(fe))
        except ValueError as ve:
            raise RepositoryException("Invalid value in file" + str(ve))
        finally:
            if file:
                file.close()

    def write_to_file(self):
        try:
            with open(self.__file_name, "w") as file:
                for element in self.get_all():
                    location_string = element.get_date().strftime("%Y-%m-%d")
                    concert_string = f"{element.get_id()},{element.get_name()},{element.get_location()},{location_string}"
                    file.write(concert_string + "\n")
        except FileNotFoundError as fe:
            raise RepositoryException("File not found " + str(fe))

    def add(self, element):
        """
        Add new element to the list of concerts
        :param element:
        :return:
        """

        self.__elements.append(element)

    def get_all(self):
        return self.__elements

    def find_by_id(self, concert_id):
        """
        FInds a singer by id
        :return:
        """
        for concert in self.__elements:
            if concert.get_id() == concert_id:
                return concert
        raise RepositoryException(f"Concert with id={concert_id} not found")

    def __len__(self):
        return len(self.__elements)


def test_repo_read():
    repo = ConcertFileRepository("/Users/maliimregergely/mig/seminar-fp/concerts.txt")
    assert len(repo.get_all()) == 2
    ...


def test_repo_write():
    repo = ConcertFileRepository("/Users/maliimregergely/mig/seminar-fp/concerts.txt")
    repo.write_to_file()
    date = datetime.strptime("2023-11-23", "%Y-%m-%d")
    repo.add(Concert(3, "Boom", "Madrid", date))
    repo.write_to_file()


if __name__ == "__main__":
    test_repo_read()
    test_repo_write()
