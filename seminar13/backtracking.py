from typing import List

"""
A = {0, 1, ... n}
l=[x0,x1,...xm], (x[i]+x[i+1])%2=1, i in {0,.. n-1}

S = A^m, card(S) = n^m
"""


def is_consistent(elements: List[int]) -> bool:
    for i in range(len(elements) - 1):
        if (elements[i] + elements[i + 1]) % 2 != 1:
            return False
    return True


def is_solution(elements: List[int], m) -> bool:
    return len(elements) == m


def back_recursive(elements: List[int], n: int, m: int):
    if is_solution(elements, m):
        print(elements)
        return
    for element in range(n):
        elements.append(element)
        if is_consistent(elements):
            back_recursive(elements, n, m)
        elements.pop()


def back_rec_wrapper(n, m):
    back_recursive([], n, m)


if __name__ == '__main__':
    back_rec_wrapper(3, 3)
