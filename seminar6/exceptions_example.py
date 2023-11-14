def my_lovely_function(x):
    print("I am being called")
    if x < 0:
        print("doing something risky")
        raise IndexError("x was smaller than 0")
    print("happy happy")


def wrapper(x):
    print("I am gonna call the other one")
    my_lovely_function(10)
    print("Yay I called it")
    print("I'm gonna do it again")
    try:
        print("before")
        my_lovely_function(1)
        print("aaaaaaaaaaaaaa")
    except ValueError as e:
        print(f"something went wrong: {e}")
    except KeyError:
        print("something else went wrong")
    finally:
        print("I am getting done no matter what")

    print("everything was fine")


if __name__ == "__main__":
    wrapper(-1)
