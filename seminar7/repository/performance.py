class PerformanceRepository:
    def __init__(self):
        self.__elements = []

    def add(self, element):
        """
        Add new element to the list of concerts
        :param element:
        :return:
        """

        self.__elements.append(element)

    def get_all(self):
        """
        Return all performances
        :return:
        """
        return self.__elements

    def __len__(self):
        return len(self.__elements)
