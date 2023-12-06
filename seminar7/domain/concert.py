class Concert:
    def __init__(self, concert_id, name, location, date):
        self.id = concert_id
        self.__name = name
        self.__location = location
        self.__date = date

    def get_id(self):
        return self.id

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_date(self):
        return self.__date

    def __str__(self):
        return f"Concert(name={self.get_name()},loc={self.get_location()},date={self.get_date()})"

    def __repr__(self):
        return str(self)
