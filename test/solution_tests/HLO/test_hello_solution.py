import pytest

from lib.solutions.HLO.hello_solution import HelloSolution


class TestHelloSolution():
    def test_hello_success(self):
        # assert HelloSolution().hello("Linda") == "Hello Linda"
        assert HelloSolution().hello("Linda") == "Hello, World!"

    def test_hello_error(self):
        with pytest.raises(TypeError):
            HelloSolution().hello(2)


