from src.pre_built.counter import count_ocurrences


def test_count_ocurrences_of_world_python():
    assert count_ocurrences("data/jobs.csv", "Python") == 1639


def test_count_ocurrences_of_world_javascript():
    assert count_ocurrences("data/jobs.csv", "Javascript") == 122
    