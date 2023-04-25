import pytest
from app.calc import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_success(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_substraction_success(self):
        assert self.calc.subtraction(self, 6, 2) ==4

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def teardown_method(self):
        print('Выполнение метода Taerdown')