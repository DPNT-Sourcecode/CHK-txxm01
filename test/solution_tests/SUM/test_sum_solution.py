import pytest

from lib.solutions.SUM.sum_solution import SumSolution


class TestSum():
    def test_sum(self):
        assert SumSolution().compute(1, 2) == 3

    def test_sum_error(self):
        with pytest.raises(TypeError):
            SumSolution().compute('a', 2)

    def test_sum_error_negative_number(self):
        with pytest.raises(ValueError):
            SumSolution().compute(-3, 2)

    def test_sum_error_number_above_100(self):
        with pytest.raises(ValueError):
            SumSolution().compute(3, 105)


