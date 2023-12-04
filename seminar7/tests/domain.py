from seminar7.domain import Singer


def test_singer():
    singer = Singer(1, "Eminem", "rap")
    assert singer.get_name() == "Eminem"
    assert singer.get_id() == 1
    assert singer.get_genre() == "rap"
    assert str(singer) == "Singer(id=1,name=Eminem,genre=rap)"

    assert singer != Singer(2, "Eminem", "rap")
    assert singer == Singer(1, "Eminem", "rap")


# TODO add tests for other entities


if __name__ == "__main__":
    test_singer()
