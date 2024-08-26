from src.pre_built.counter import count_ocurrences


def test_counter():
    consoles = count_ocurrences("data/jobs.csv", "Python")
    assert consoles == 1639
    
    consoles = count_ocurrences("data/jobs.csv", "Javascript")
    assert consoles == 122
