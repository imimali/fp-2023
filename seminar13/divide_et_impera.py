from typing import List


def power(x: int, exponent: int) -> int:
    """
    x^n = (x^n/2)^2
    ((x*x)*(x*x))(...*x)
    Raise x to the power exponent
    :param x:
    :param exponent:
    :return:
    """
    if exponent == 0:
        return 1
    result = power(x, exponent // 2)
    if exponent % 2 == 0:
        return result * result
    return result * result * x


def check_sortedness(elements: List[int]) -> bool:
    """
    [(1,2,3,4,5),((6,7),(6,8,9))]
    Returns true if all elements of the list are
    in ascending order
    :param elements:
    :return:

    T(n) = | 1, n <= 1
           | 2T(n/2) + 1 = 2(2T(n/2^2)+1)+1 = 1 + 2 + ... + 2^k
                                            = 2*2^(k) - 1
                                            = 2*2^(log2(n)) -1
                                            = 2n - 1 \in Theta(n), n>1

    n=2^k => log2(n)
    """

    if len(elements) <= 1:
        return True
    middle = len(elements) // 2
    left = elements[:middle]
    right = elements[middle:]
    return left[-1] < right[0] and check_sortedness(left) and check_sortedness(right)


def test_power():
    assert power(0, 0) == 1
    assert power(1, 0) == 1
    assert power(-1, 0) == 1
    assert power(1, 2) == 1
    assert power(2, 1) == 2
    assert power(2, 2) == 4
    assert power(2, 5) == 32


def test_check_sortedness():
    assert check_sortedness([]) == True
    assert check_sortedness([1]) == True
    assert check_sortedness([1, 2]) == True
    assert check_sortedness(list(range(10))) == True
    assert check_sortedness([1, 2, 3, 5, 2, 1]) == False


if __name__ == '__main__':
    test_power()
    test_check_sortedness()
