class SingerRepository:
    def __init__(self):
        self.__elements = []

    def add(self, element):
        """
        Add new element to the list of singers
        :param element:
        :return:
        """

        self.__elements.append(element)

    def get_all(self):
        return self.__elements

    def __len__(self):
        return len(self.__elements)
