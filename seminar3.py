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


def get_name(fruit):
    return fruit[0]


def get_color(fruit):
    return fruit[1]


def get_weight(fruit):
    return fruit[2]


def set_name(fruit, name):
    fruit[0] = name


def set_color(fruit, color):
    fruit[1] = color


def set_weight(fruit, weight):
    fruit[2] = weight


def create_fruit_from_str(fruit_str):
    fruit = fruit_str.split(",")
    fruit[2] = int(fruit[2])
    return fruit


def add_fruit_to_list(fruit_list, fruit):
    """
    Adds a new fruit to a list
    :param fruit_list: list of fruits
    :param fruit: fruit entity
    :return: nothing
    possible exceptions
    """
    fruit_list.append(fruit)


def test_add_fruit_to_list():
    fruit_list = []
    fruit = ["pineapple", "green", 998]
    fruit1 = ["pineapple 1 ", "green 1", 998]
    add_fruit_to_list(fruit_list, fruit)
    assert fruit_list[0] == fruit
    assert len(fruit_list) == 1
    add_fruit_to_list(fruit_list, fruit1)
    assert fruit_list[0] == fruit
    assert fruit_list[1] == fruit1
    assert len(fruit_list) == 2


def filter_by_color(fruits_list, color):
    """
    Filters a list of fruits by color
    :param fruits_list: list of fruits to filter
    :param color: color to filter by, string
    :return: list of fruits having `color` as color
    exceptions...
    """
    result = []
    for fruit in fruits_list:
        if get_color(fruit) == color:
            result.append(fruit)
    return result


def test_filter_by_color():
    fruit = ["pineapple", "green", 998]
    fruit_list = [fruit]
    fruit_list.append(["grapes", "black", 123])
    fruit_list.append(["mandarin", "black", 99])
    assert filter_by_color([], "black") == []
    assert filter_by_color(fruit_list, "skyblue") == []
    assert filter_by_color(fruit_list, "green") == [["pineapple", "green", 998]]
    assert filter_by_color(fruit_list, "black") == [
        ["grapes", "black", 123],
        ["mandarin", "black", 99],
    ]


def read_fruit():
    fruit = [None] * 3
    name = input("Enter name:")
    set_name(fruit, name)

    color = input("Enter color:")
    set_color(fruit, color)

    weight = int(input("Enter weight:"))
    set_weight(fruit, weight)

    return fruit


def main():
    fruits = []
    options = {1: filter_by_color}
    while True:
        print(
            """
        1. Citește date
        2. Filtrează după culoare
        3. Afișare sumă greutate
        0. Exit
        """
        )
        option = int(input("Enter option:"))
        if option == 0:
            print("Bye")
            break
        if option == 1:
            fruit = read_fruit()
            add_fruit_to_list(fruits, fruit)
        if option == 2:
            print(filter_by_color(fruits, input("Enter color:")))


if __name__ == "__main__":
    test_add_fruit_to_list()
    test_filter_by_color()
    main()
