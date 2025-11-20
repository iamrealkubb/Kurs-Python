from points import Point
import math

class Circle:

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * self.radius ** 2

    def move(self, x, y):
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):
        # wektor miedzy srodkami okregow i jego dlugosc czyli dystans
        dystans_x = self.pt.x - other.pt.x
        dystans_y = self.pt.y - other.pt.y
        dystans = math.sqrt(pow(dystans_x, 2) + pow(dystans_y, 2))

        # specjalny przypadek gdy dystans to 0 -> wtedy okregi maja srodek w tym samym miejscu
        if dystans == 0:
            return Circle(self.pt.x, self.pt.y, max(self.radius, other.radius))

        # obliczenie promienia nowego okregu
        nowy_promien = round((dystans + self.radius + other.radius) / 2, 4) # z zaokrogleniem do 4 miejsc

        # skala do przesuniecia srodka nowego okregu
        skala = round((nowy_promien - self.radius) / dystans, 4)

        # wspolrzedne srodka nowego okregu
        nowy_x = round(self.pt.x + skala * (other.pt.x - self.pt.x), 4)
        nowy_y = round(self.pt.y + skala * (other.pt.y - self.pt.y), 4)

        return Circle(nowy_x, nowy_y, nowy_promien)

import unittest

class TestCircle(unittest.TestCase):

    def setUp(self):
        # kilka okregow do testow
        self.c1 = Circle(0, 0, 1)
        self.c2 = Circle(3, 4, 2)
        self.c3 = Circle(0, 0, 1)

    def test_init(self):
        c = Circle(1, 2, 3)
        self.assertEqual(c.pt.x, 1)
        self.assertEqual(c.pt.y, 2)
        self.assertEqual(c.radius, 3)

        with self.assertRaises(ValueError): # sprawdzenie wyjatku przy ujemnym promieniu
            Circle(0, 0, -1)

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(0, 0, 1)")
        self.assertEqual(repr(self.c2), "Circle(3, 4, 2)")

    def test_eq(self):
        self.assertTrue(self.c1 == self.c3)
        self.assertFalse(self.c1 == self.c2)

    def test_ne(self):
        self.assertTrue(self.c1 != self.c2)
        self.assertFalse(self.c1 != self.c3)

    def test_area(self):
        self.assertAlmostEqual(self.c1.area(), math.pi * 1 ** 2)
        self.assertAlmostEqual(self.c2.area(), math.pi * 2 ** 2)

    def test_move(self):
        self.c1.move(5, -3)
        self.assertEqual(self.c1.pt.x, 5)
        self.assertEqual(self.c1.pt.y, -3)

    def test_cover(self):
        okrag_pokrywajacy = self.c1.cover(self.c2)

        dystans_x = self.c2.pt.x - self.c1.pt.x
        dystans_y = self.c2.pt.y - self.c1.pt.y
        dystans = math.sqrt(dystans_x ** 2 + dystans_y ** 2)

        oczekiwany_promien = round((dystans + self.c1.radius + self.c2.radius) / 2, 4)

        skala = round((oczekiwany_promien - self.c1.radius) / dystans, 4)
        oczekiwany_x = round(self.c1.pt.x + skala * dystans_x, 4)
        oczekiwany_y = round(self.c1.pt.y + skala * dystans_y, 4)

        self.assertAlmostEqual(okrag_pokrywajacy.radius, oczekiwany_promien, places=4)
        self.assertAlmostEqual(okrag_pokrywajacy.pt.x, oczekiwany_x, places=4)
        self.assertAlmostEqual(okrag_pokrywajacy.pt.y, oczekiwany_y, places=4)

        # pokrycie identycznych okregow powinno zwrocic ten sam promien i srodek
        okrag_pokrywajacy2 = self.c1.cover(self.c3)
        self.assertEqual(okrag_pokrywajacy2.radius, self.c1.radius)
        self.assertEqual(okrag_pokrywajacy2.pt.x, self.c1.pt.x)
        self.assertEqual(okrag_pokrywajacy2.pt.y, self.c1.pt.y)

    def tearDown(self):
        del self.c1
        del self.c2
        del self.c3

if __name__ == '__main__':
    unittest.main()