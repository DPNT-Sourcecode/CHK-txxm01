import pytest

from lib.solutions.SUM.sum_solution import SumSolution


class TestSum():
    def setUp(self):
        self.sum_solution = SumSolution()

    def test_sum(self):
        assert self.sum_solution.compute(1, 2) == 3

    def test_sum_error(self):
        with pytest.raises(TypeError):
            SumSolution().compute('a', 2)
