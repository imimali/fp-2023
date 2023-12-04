from .singer import Singer
from .concert import Concert


class Performance:
    def __init__(self, singer: Singer, concert: Concert):
        self.__singer = singer
        self.__concert = concert

    def get_singer(self):
        return self.__singer

    def get_concert(self):
        return self.__concert

    def __str__(self):
        return f"Performance(s={self.__singer}, c={self.__concert})"

    def __repr__(self):
        return str(self)
