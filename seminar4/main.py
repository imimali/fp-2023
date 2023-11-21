from seminar4.business import add_fruit_to_list, filter_by_color, compute_sum_of_weights
from seminar4.tests import tests_main

"""
Scrieți o aplicație pentru a gestiona o listă de fructe.
Fiecare fruct o să aibă un nume, culoare, și greutate.
Aplicația să permită următoarele funcționalități:
1. adăugare fructe: utilizatorul introduce detaliile fructelor
și aplicația le adaugă în listă
2. filtrare după culoare: utilizatorul introduce o culoare
iar aplicația afișează acele fructe care sunt de culoarea
respectivă
3. afișarea sumei greutății tuturor fructelor
"""


def read_fruit_from_console():
    """
    Reads a fruit from console
    :return: fruit in string form, fields separated by comma
    """
    return input("Enter name, color, weight separated by comma: ")


def create_fruit_from_str(fruit_str):
    """
    Creates a fruit from a string

    :param fruit_str: comma-separated string of fruit data
    :return: fruit in representation
    """
    fruit = fruit_str.split(",")
    fruit[2] = int(fruit[2])
    # set_weight(fruit, int(get_weight(fruit))) # alternatively
    return fruit


def add_fruit_ui(fruits):
    """
    Reads a fruit from console and adds it to the list
    :param fruits: list of fruits to which to add
    :return: nothing
    """
    raw_fruit = read_fruit_from_console()
    fruit = create_fruit_from_str(raw_fruit)
    add_fruit_to_list(fruits, fruit)
    print(f"{fruit} Adăugat cu succes")


def main():
    fruits = []
    while True:
        print(
            """
        1. Adaugă fruct
        2. Filtrează după culoare
        3. Afișare sumă greutate
        0. Exit
        """
        )
        print(fruits)
        option = int(input("Enter option:"))
        if option == 0:
            print("Bye")
            break
        if option == 1:
            add_fruit_ui(fruits)
        if option == 2:
            print(filter_by_color(fruits, input("Enter color:")))
        if option == 3:
            print(f"The sum of weights is  {compute_sum_of_weights(fruits)}")


if __name__ == "__main__":
    tests_main()
    main()
