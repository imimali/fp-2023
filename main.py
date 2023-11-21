"""
Scrieți o aplicație de tip consolă care are următoarele funcționalități:
1. Citirea unei liste de numere întregi de la tastatură.
2. Afișarea sumei tuturor numerelor pozitive pare din listă.
3. Afișarea produselor tuturor numerelor prime
4. Afișarea primelor k cele mai mici numere, unde k e un număr citit de la tastatură
"""


def print_menu():
    print(
        """
    1. Citește o liste de numere întregi de la tastatură.
    2. Afișează suma tuturor numerelor pozitive pare din listă.
    3. Afișează produsele tuturor numerelor prime
    4. afișează primele k cele mai mici numere, unde k e un număr citit de la tastatură
    5. print list
    6. help
    0. Exit
    """
    )


def read_list():
    raw_list = input("Enter list: ")
    string_list = raw_list.split(" ")
    result = []
    for number in string_list:
        result.append(int(number))
    return result


def read_number():
    return int(input("Enter number: "))


def first_k_min(numbers_list, k):
    sorted_numbers = sorted(numbers_list)
    return sorted_numbers[:k]


def positive_even_sum(initial_number):
    """
    Filters a list of numbers and returns another list containing only the even positive numbers
    :param initial_number: list of integers
    :return: list containing positive even numbers
    """
    result = []
    for number in initial_number:
        if number > 0 and number % 2 == 0:
            result.append(number)
    return sum(result)


def prim(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for divisor in range(3, x // 2, 2):
        if x % divisor == 0:
            return False
    return True


def filter_primes(initial_numbers):
    return list(filter(prim, initial_numbers))


def list_product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def product_primes(numbers):
    primes = filter_primes(numbers)
    return list_product(primes)


def test_positive_even_sum():
    assert positive_even_sum([1, 2, 3]) == 2
    # TODO complete with other test cases


def test_prim():
    assert prim(1) == False
    assert prim(-1) == False
    assert prim(2)
    assert not prim(4)
    assert prim(5)
    assert prim(7)
    assert not prim(9)


def main():
    numbers = [1, 2, 4, 5, 6, 10, 12, -10, 4, -56]
    print_menu()
    while True:
        option = int(input("Choose(or 6 to print menu): "))
        if option == 0:
            print("Bye")
            return
        elif option == 1:
            numbers = read_list()
            print("List read successfully")

        elif option == 2:
            even_positive_sum = positive_even_sum(numbers)
            print(f"The sum of even positives is: {even_positive_sum}")

        elif option == 3:
            prod = product_primes(numbers)
            print(f"The primes are: {prod}")

        elif option == 4:
            k = read_number()
            print(f"The first {k} mins are", first_k_min(numbers, k))

        elif option == 5:
            print(f"The numbers are: ", numbers)
        elif option == 6:
            print_menu()
        else:
            print("Invalid option")


if __name__ == "__main__":
    test_positive_even_sum()
    test_prim()
    main()
