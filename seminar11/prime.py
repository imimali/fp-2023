import math


def is_prime(x: int) -> bool:
    """
    Checks if a positive number x is prime or not
    :param x:
    :return: True if the number if prime, False otherwise
    """
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for d in range(3, int(math.sqrt(x)) + 1, 2):
        if x % d == 0:
            return False
    return True
