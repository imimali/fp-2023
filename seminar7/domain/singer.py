class Singer:
    def __init__(self, singer_id, name, genre):
        self.__id = singer_id
        self.__name = name
        self.__genre = genre

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_genre(self):
        return self.__genre

    def __str__(self):
        return f"Singer(id={self.__id},name={self.__name},genre={self.__genre})"

    def __eq__(self, other):
        if not isinstance(other, Singer):
            return False
        return self.get_id() == other.get_id()
