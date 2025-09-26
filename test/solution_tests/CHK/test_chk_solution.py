import pytest

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutSolution():
    def test_checkout_success(self):
        print(CheckoutSolution().checkout("A B"))
        assert CheckoutSolution().checkout("A B") == 80

    # def test_hello_error(self):
    #     with pytest.raises(TypeError):
    #         HelloSolution().hello(2)
