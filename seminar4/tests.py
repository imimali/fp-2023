from seminar4.business import add_fruit_to_list, filter_by_color, compute_sum_of_weights


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


def test_compute_sum():
    fruit_list = [["pineapple", "green", 998]]
    assert compute_sum_of_weights(fruit_list) == 998
    try:
        compute_sum_of_weights([])
        assert False
    except ValueError:
        assert True

    fruit_list = [["pineapple", "green", 998], ["pineapple", "green", 2]]
    assert compute_sum_of_weights(fruit_list) == 1000


def tests_main():
    test_add_fruit_to_list()
    test_filter_by_color()
    test_compute_sum()
