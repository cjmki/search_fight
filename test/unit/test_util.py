from src.util.argv_util import read_argv
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (["main.py", "jeff bezos", "aaron swartz", "elon musk"], 3),
        (["main.py", "aaron swartz", "elon musk"], 2),
    ],
)
def test_read_argv_len(test_input, expected):
    args = read_argv(test_input)
    assert len(args) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ["main.py", "jeff bezos", "aaron swartz", "elon musk"],
            ["jeff bezos", "aaron swartz", "elon musk"],
        )
    ],
)
def test_read_argv_output(test_input, expected):
    args = read_argv(test_input)
    assert args == expected
