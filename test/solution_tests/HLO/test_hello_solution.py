import pytest

from lib.solutions.HLO.hello_solution import HelloSolution


class TestHelloSolution():
    def test_hello_success(self):
        assert HelloSolution().hello("Linda") == "Hello Linda"

    def test_hello_error(self):
        with pytest.raises(TypeError):
            HelloSolution().hello(2)

    # def test_sum_error_negative_number(self):
    #     with pytest.raises(ValueError):
    #         SumSolution().compute(-3, 2)

    # def test_sum_error_number_above_100(self):
    #     with pytest.raises(ValueError):
    #         SumSolution().compute(3, 105)

