from seminar7.service import SingerService
from seminar7.domain import ValidatorException


class UI:
    def __init__(self):
        self.__service = SingerService()

    def __print_menu(self):
        print(
            """
            1 - Add new singer
            2 - See all
            0 - Exit
        """
        )

    def __read_command(self):
        return input("Enter command: ")

    def __read_valid_int(self, message):
        try:
            return int(input(message))
        except ValueError:
            print("Invalid value. Try again!")
            return self.__read_valid_int(message)

    def run(self):
        self.__print_menu()
        while True:
            try:
                command = self.__read_command()
                if command == "1":
                    singer_id = self.__read_valid_int("Enter id: ")
                    name = input("Name: ")
                    genre = input("Genre: ")
                    self.__service.add(singer_id, name, genre)

                elif command == "0":
                    break
            except ValidatorException as v:
                print(f"Invalid data encountered: {v}")
            except ValueError:
                print("Invalid value was introduced")
            except Exception as e:
                print(f"Something went wrong: {e}")


if __name__ == "__main__":
    UI().run()
