class Flight:
    def __init__(self, code, duration, departure, destination):
        self.__code = code
        self.__duration = duration
        self.__departure = departure
        self.__destination = destination

    def get_code(self):
        return self.__code

    def get_duration(self):
        return self.__duration

    def get_departure(self):
        return self.__departure

    def get_destination(self):
        return self.__destination

    def set_duration(self, duration):
        self.__duration = duration

    def __eq__(self, other):
        if not isinstance(other, Flight):
            return False
        return self.__code == other.get_code()
