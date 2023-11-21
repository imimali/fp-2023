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


def add_fruit_to_list(fruit_list, fruit):
    """
    Adds a new fruit to a list
    :param fruit_list: list of fruits
    :param fruit: fruit entity
    :return: nothing
    possible exceptions
    """
    fruit_list.append(fruit)


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


def compute_sum_of_weights(fruit_list):
    """
    Compute the sum of weights for all fruits
    :param fruit_list: list of fruits
    :return: the sum of weights of all fruits in the list
    :throws ValueError if there are no fruits in the list
    """
    if not fruit_list:
        raise ValueError("No fruits in the list")
    # total = 0
    # for fruit in fruit_list:
    #     total += get_weight(fruit)
    # return total
    return sum(map(get_weight, fruit_list))
