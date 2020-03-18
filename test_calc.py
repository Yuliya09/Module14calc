import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        "Сложение"
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        "Вычитание"
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        "Умножение"
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        "Деление"
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_oper_neg(self):
        """Негативный, возведение в степень"""
        self.assertEqual(calc_me(4, 2,"**"), 'ERROR: Unknown operation')

    def test_number1(self):
        "Негативный. Если x не присвоили значение"
        self.assertEqual(calc_me(x=None), 'ERROR: send me Number1')

    def test_number2(self):
        "Негативный. Если y не присвоили значение"
        self.assertEqual(calc_me(x=1,y=None), 'ERROR: send me Number2')

if __name__ == '__main__':
    unittest.main(verbosity=2)