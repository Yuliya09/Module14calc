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

    def test_oper(self):
        """Возведение в степень"""
        self.assertEqual(calc_me(4, 2,"^"), 16)

    def test_number1(self):
        "Негативный. Если x не присвоили значение"
        self.assertEqual(calc_me(x=None, y=0), 'ERROR: send me Number1')

    def test_number2(self):
        "Негативный. Если y не присвоили значение"
        self.assertEqual(calc_me(x=1,y=None), 'ERROR: send me Number2')

    def test_number1_2(self):
        "Негативный. Если x и y не присвоили значение"
        self.assertEqual(calc_me(x=None,y=None), 'ERROR: send me Number1')

    def test_number_s1(self):
        "Негативный. Если x присвоили символьное значение"
        self.assertEqual(calc_me(x="!", y=1), 'ERROR: now it is does not supported')

    def test_number_s2(self):
        "Негативный. Если y присвоили символьное значение"
        self.assertEqual(calc_me(x=0,y="D"), 'ERROR: now it is does not supported')

    def test_number_s1_2(self):
        "Негативный. Если x и y присвоили символьное значение"
        self.assertEqual(calc_me(x="O",y="&"), 'ERROR: now it is does not supported')

if __name__ == '__main__':
    unittest.main(verbosity=2)