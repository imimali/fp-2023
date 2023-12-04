from datetime import datetime
from seminar7.domain import Singer
from seminar7.repository.exceptions import RepositoryException


class SingerFileRepository:
    def __init__(self, file_name: str):
        self.__elements = []
        self.__file_name = file_name
        self.__read_singers()

    def __read_singers(self):
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
                singer_id = int(components[0])
                name = components[1]
                genre = components[2]
                self.__elements.append(Singer(singer_id, name, genre))

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
                    singer_string = (
                        f"{element.get_id()},{element.get_name()},{element.get_genre()}"
                    )
                    file.write(singer_string + "\n")
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

    def find_by_id(self, singer_id):
        """
        FInds a singer by id
        :return:
        """
        for singer in self.__elements:
            if singer.get_id() == singer_id:
                return singer
        raise RepositoryException(f"Singer with id={singer_id} not found")

    def __len__(self):
        return len(self.__elements)
