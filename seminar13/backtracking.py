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


def back_recursive_with_collector(current_elements: List[int], n: int, m: int, solutions=None):
    solutions = solutions if solutions is not None else []
    if is_solution(current_elements, m):
        solutions.append(current_elements[:])
        return
    for element in range(n):
        current_elements.append(element)
        if is_consistent(current_elements):
            back_recursive_with_collector(current_elements, n, m, solutions)
        current_elements.pop()


def back_rec_wrapper(n, m):
    back_recursive([], n, m)


def back_rec_collector_wrapper(n, m):
    solutions = []
    back_recursive_with_collector([], n, m, solutions)
    return solutions


def back_iterative(n: int, m: int):
    solutions = []  # we collect the solutions here instead of simply printing them
    stack = [[]]
    while stack:
        elements = stack.pop()
        if is_solution(elements, m):
            solutions.append(elements)
            continue
        # here we get through the possible values one by one.
        # For example, for the problem with collinearity, you'd
        # go through the list of points, for the problems with given
        # number lists, you'd go through the list of numbers, etc.
        # This is a more straightforward and flexible way than what
        # that `x[-1] = x[-1] + 1` in the lecture did
        for element in range(n):
            new_elements = elements + [element]
            # the + operator implicitly creates a new list, no
            # need to copy new_elements again
            if is_consistent(new_elements):
                stack.append(new_elements)
    return solutions


if __name__ == '__main__':
    print(back_rec_collector_wrapper(3, 3))
    print(back_iterative(3, 3))
    # find_lists(3, 3)
