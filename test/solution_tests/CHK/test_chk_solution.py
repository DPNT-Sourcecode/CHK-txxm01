import pytest

from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckoutSolution():
    def test_checkout_success(self):
        print(CheckoutSolution().checkout("A B EE"))
        assert CheckoutSolution().checkout("A B EE") == 130

    # def test_checkout_success_not_spaces(self):
    #     assert CheckoutSolution().checkout("AC") == 70

    # def test_checkout_fail_invalid_input(self):
    #     assert CheckoutSolution().checkout("CFG") == -1

    # def test_checkout_fail_input_int(self):
    #     assert CheckoutSolution().checkout(100) == -1



