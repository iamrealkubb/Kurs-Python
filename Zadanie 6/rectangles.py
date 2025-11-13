from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return (self.pt1 == other.pt1 and self.pt2 == other.pt2) or \
            (self.pt1 == other.pt2 and self.pt2 == other.pt1)

    def __ne__(self, other):
        return not self == other

    def center(self):
        cx = (self.pt1.x + self.pt2.x) / 2
        cy = (self.pt1.y + self.pt2.y) / 2
        return Point(cx, cy)

    def area(self):
        szerokosc = abs(self.pt2.x - self.pt1.x)
        wysokosc = abs(self.pt2.y - self.pt1.y)
        return szerokosc * wysokosc

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

import unittest

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(0, 0, 4, 5)
        self.r2 = Rectangle(4, 5, 0, 0)
        self.r3 = Rectangle(-2, -3, 2, 3)
        self.r4 = Rectangle(1, 1, 3, 2)

    def test_str(self):
        self.assertEqual(str(self.r1), "[(0, 0), (4, 5)]")
        self.assertIn("4", str(self.r2))
        self.assertIn("5", str(self.r2))

    def test_repr(self):
        self.assertEqual(repr(self.r1), "Rectangle(0, 0, 4, 5)")
        self.assertEqual(repr(self.r3), "Rectangle(-2, -3, 2, 3)")

    def test_eq(self):
        self.assertTrue(self.r1 == self.r2)
        self.assertFalse(self.r1 == self.r3)
        self.assertTrue(self.r1 != self.r3)
        self.assertFalse(self.r1 != self.r2)
        self.assertFalse(self.r1 == "lorem ipsum")  # porównanie z innym typem

    def test_ne(self):
        self.assertTrue(self.r1 != self.r3)
        self.assertFalse(self.r1 != self.r2)

    def test_center(self):
        c1 = self.r1.center()
        self.assertIsInstance(c1, Point)
        self.assertEqual(c1, Point(2, 2.5))
        c3 = self.r3.center()
        self.assertEqual(c3, Point(0, 0))

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r3.area(), 24)
        self.assertEqual(self.r4.area(), 2)

    def test_move(self):
        self.r4.move(2, 3)
        self.assertEqual(self.r4.pt1, Point(3, 4))
        self.assertEqual(self.r4.pt2, Point(5, 5))
        wczesniej = Rectangle(self.r1.pt1.x, self.r1.pt1.y, self.r1.pt2.x, self.r1.pt2.y)
        self.r1.move(0, 0)
        self.assertEqual(self.r1.pt1, wczesniej.pt1)
        self.assertEqual(self.r1.pt2, wczesniej.pt2)

    def tearDown(self):
        del self.r1
        del self.r2
        del self.r3
        del self.r4

if __name__ == '__main__':
    unittest.main()