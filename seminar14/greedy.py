from collections import namedtuple
from typing import List

Element = namedtuple('Element', 'weight value')


def knapsack(elements: List[Element], max_capacity: int):
    """
    :param elements:
    :param max_capacity: max weight allowed in the knapsack
    :return:
    """
    elements.sort(key=lambda x: x.value / x.weight)
    solution = []
    while (current_sum := sum(map(lambda x: x.weight, solution))) < max_capacity and elements:
        element_to_add = elements.pop()
        if current_sum + element_to_add.weight <= max_capacity:
            solution.append(element_to_add)
    return sum(map(lambda x: x.value, solution))
from functools import lru_cache

@lru_cache(maxsize=1000)
def fibo(n):
 if n<=2: return 1
 return fibo(n-1)+fibo(n-2)

if __name__ == '__main__':
    objects = [
        Element(weight=10, value=1),
        Element(weight=3, value=10),
        Element(weight=6, value=3),
        Element(weight=2, value=7),
        Element(weight=1, value=8),
    ]
    print(knapsack(objects, 4))
