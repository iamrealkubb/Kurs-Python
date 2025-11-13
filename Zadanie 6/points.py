import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            raise TypeError("other musi byc typu Point")
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        nowy_x = self.x + other.x
        nowy_y = self.y + other.y
        return Point(nowy_x, nowy_y)

    def __sub__(self, other):
        nowy_x = self.x - other.x
        nowy_y = self.y - other.y
        return Point(nowy_x, nowy_y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)) # pierwiastek(x^2 + y^2)

    def __hash__(self):
        return hash((self.x, self.y))

import unittest

class TestPoint(unittest.TestCase):

    def setUp(self): # przykladowe punkty do testow
        self.o = Point(0, 0)
        self.a = Point(3, 4)
        self.b = Point(-1, 2)
        self.c = Point(3.0, 4.0)
        self.d = Point(0, -5)

    def test_str(self):
        self.assertEqual(str(self.o), "(0, 0)")
        self.assertEqual(str(self.a), "(3, 4)")
        self.assertIn("3", str(self.c))
        self.assertEqual(str(self.d), "(0, -5)")

    def test_repr(self):
        self.assertEqual(repr(self.o), "Point(0, 0)")
        self.assertEqual(repr(self.a), "Point(3, 4)")
        self.assertEqual(repr(self.c), "Point(3.0, 4.0)")

    def test_eq(self):
        self.assertTrue(self.a == self.c)
        self.assertTrue(self.c == self.a)
        self.assertTrue(self.a == Point(3, 4))
        self.assertTrue(self.a == self.a)
        with self.assertRaises(TypeError):
            _ = self.a == (3, 4)  # porownanie z innym typem wiec TypeError

    def test_ne(self):
        self.assertTrue(self.a != self.b)
        self.assertFalse(self.a != Point(3, 4))

    def test_add(self):
        r = self.a + self.b
        self.assertIsInstance(r, Point)
        self.assertEqual(r.x, 3 + (-1))
        self.assertEqual(r.y, 4 + 2)
        self.assertIsNot(r, self.a)
        self.assertIsNot(r, self.b)

    def test_sub(self):
        r = self.a - self.b
        self.assertEqual(r.x, 3 - (-1))
        self.assertEqual(r.y, 4 - 2)

    def test_mul(self):
        self.assertEqual(self.a * self.b, 5)
        self.assertEqual(self.a * self.b, self.b * self.a)
        self.assertEqual(self.o * self.a, 0)
        p = Point(0.5, -1.5)
        oczekiwany = 3 * 0.5 + 4 * (-1.5)
        self.assertAlmostEqual(self.a * p, oczekiwany)

    def test_cross(self):
        self.assertEqual(self.a.cross(self.b), 10)
        self.assertEqual(self.b.cross(self.a), -10)
        self.assertEqual(self.o.cross(self.a), 0)

    def test_length(self):
        self.assertAlmostEqual(self.a.length(), 5.0)
        self.assertAlmostEqual(self.d.length(), 5.0)
        p = Point(1.5, math.sqrt(2.75))
        oczekiwany = math.hypot(1.5, math.sqrt(2.75))
        self.assertAlmostEqual(p.length(), oczekiwany)
        self.assertAlmostEqual(self.o.length(), 0.0)

    def test_hash(self):
        p1 = Point(100, 200)
        p2 = Point(100, 200)
        self.assertTrue(p1 == p2)
        self.assertEqual(hash(p1), hash(p2))

    def tearDown(self):
        del self.o
        del self.a
        del self.b
        del self.c
        del self.d

if __name__ == '__main__':
    unittest.main()