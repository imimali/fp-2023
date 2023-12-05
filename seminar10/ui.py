from seminar10.repository import RepositoryError


class UI:
    def __init__(self, service):
        self.__service = service

    def menu(self):
        print(
            """
        1. Add new flight
        2. Remove a flight
        0. Exit
        """
        )

    def add_flight(self):
        code = input("Enter flight code")
        duration = int(input("Enter duration"))
        departure = input("Enter departure city")
        destination = input("Enter destination city")
        self.__service.add(code, duration, departure, destination)

    def remove_flight(self):
        code = input("Enter flight code")
        self.__service.remove(code)

    def main(self):
        while True:
            try:
                self.menu()
                command = input("Enter option: ")
                if command == "1":
                    self.add_flight()
                if command == "2":
                    self.remove_flight()

                if command == "3":
                    departure = input("Enter departure")
                    self.__service.get_by_departure_sorted_by_destination(departure)

                elif command == "0":
                    print("Bye")
                    break
            except ValueError as e:
                print("Error encountered:", e)

            except RepositoryError as e:
                print("Error encountered in persistence", e)
