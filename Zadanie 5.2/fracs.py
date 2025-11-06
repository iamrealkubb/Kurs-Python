from math import gcd

def simplify(frac):
    licznik, mianownik = frac
    if mianownik == 0:
        raise ValueError("mianownik nie moze byc zerem")
    if mianownik < 0:
        licznik, mianownik = -licznik, -mianownik
    nwd = gcd(abs(licznik), abs(mianownik))
    return [licznik // nwd, mianownik // nwd]

def add_frac(frac1, frac2):
    l1, m1 = frac1
    l2, m2 = frac2
    return simplify([l1 * m2 + l2 * m1, m1 * m2])

def sub_frac(frac1, frac2):
    l1, m1 = frac1
    l2, m2 = frac2
    return simplify([l1 * m2 - l2 * m1, m1 * m2])

def mul_frac(frac1, frac2):
    l1, m1 = frac1
    l2, m2 = frac2
    return simplify([l1 * l2, m1 * m2])

def div_frac(frac1, frac2):
    l1, m1 = frac1
    l2, m2 = frac2
    if l2 == 0:
        raise ValueError("nie mozna dzielic przez zero")
    return simplify([l1 * m2, m1 * l2])

def is_positive(frac):
    licznik, mianownik = simplify(frac)
    return licznik * mianownik > 0

def is_zero(frac):
    licznik, mianownik = frac
    return licznik == 0

def cmp_frac(frac1, frac2):
    l1, m1 = simplify(frac1)
    l2, m2 = simplify(frac2)
    lewa = l1 * m2
    prawa = l2 * m1
    if lewa < prawa:
        return -1
    elif lewa > prawa:
        return 1
    return 0

def frac2float(frac):
    licznik, mianownik = frac
    return licznik / mianownik

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_simplify(self):
        self.assertEqual(simplify([2, 4]), [1, 2])
        self.assertEqual(simplify([1000000, 4000000]), [1, 4])
        self.assertEqual(simplify([-2, 4]), [-1, 2])
        self.assertEqual(simplify([2, -4]), [-1, 2])
        self.assertEqual(simplify([-2, -4]), [1, 2])
        self.assertEqual(simplify([0, 5]), [0, 1])
        self.assertEqual(simplify([0, -7]), [0, 1])
        self.assertEqual(simplify([13, 17]), [13, 17])
        with self.assertRaises(ValueError):
            simplify([1, 0]) # oczekujemy wyjatku

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-1, 2], [1, 2]), self.zero)
        self.assertEqual(add_frac([1, -2], [1, 2]), self.zero)

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 3], [1, 2]), [-1, 6])
        self.assertEqual(sub_frac([-1, 2], [1, 2]), [-1, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])
        self.assertEqual(mul_frac([-1, 2], [2, 5]), [-1, 5])
        self.assertEqual(mul_frac(self.zero, [5, 9]), self.zero)

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 4]), [2, 1])
        self.assertEqual(div_frac([-3, 4], [3, 2]), [-1, 2])
        with self.assertRaises(ValueError):
            div_frac([1, 3], [0, 7])  # oczekujemy wyjatku

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-3, -4]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))
        self.assertFalse(is_positive([0, 5]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertTrue(is_zero([0, -3]))
        self.assertTrue(is_zero([0, 99]))
        self.assertFalse(is_zero([1, 100]))
        self.assertFalse(is_zero([-1, 100]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([3, 4], [2, 3]), 1)
        self.assertEqual(cmp_frac([0, 5], [0, 7]), 0)
        self.assertEqual(cmp_frac([1, -2], [-3, 4]), 1)
        self.assertEqual(cmp_frac([-1, -2], [1, 3]), 1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([1, 3]), 0.3333333)
        self.assertAlmostEqual(frac2float([-1, 4]), -0.25)
        self.assertAlmostEqual(frac2float([7, 3]), 7 / 3)
        self.assertAlmostEqual(frac2float([1, -2]), -0.5)

    def tearDown(self):
        self.zero = None

if __name__ == '__main__':
    unittest.main()