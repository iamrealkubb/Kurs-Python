import pytest
from rectangles import Rectangle
from points import Point

class TestRectangle:

    def setup_method(self):
        self.r1 = Rectangle(0, 0, 4, 5)
        self.r2 = Rectangle(4, 5, 0, 0)
        self.r3 = Rectangle(-2, -3, 2, 3)
        self.r4 = Rectangle(1, 1, 3, 2)

    def test_init_order(self):
        r = Rectangle(5, 7, 2, 3)
        assert r.left == 2
        assert r.bottom == 3
        assert r.right == 5
        assert r.top == 7

    def test_from_points(self):
        p1 = Point(0, 0)
        p2 = Point(4, 5)
        r = Rectangle.from_points((p1, p2))
        assert r.left == 0
        assert r.bottom == 0
        assert r.right == 4
        assert r.top == 5
        with pytest.raises(ValueError):
            Rectangle.from_points((p1,))
        with pytest.raises(ValueError):
            Rectangle.from_points((p1, p2, Point(1,1)))

    def test_str_repr(self):
        assert str(self.r1) == "[(0, 0), (4, 5)]"
        assert repr(self.r1) == "Rectangle(0, 0, 4, 5)"

    def test_eq_ne(self):
        assert self.r1 == self.r2
        assert self.r1 != self.r3
        assert not (self.r1 != self.r2)
        assert self.r1 != "lorem ipsum"

    def test_properties(self):
        assert self.r1.width == 4
        assert self.r1.height == 5
        assert self.r1.left == 0
        assert self.r1.right == 4
        assert self.r1.bottom == 0
        assert self.r1.top == 5
        assert self.r1.topleft == Point(0, 5)
        assert self.r1.topright == Point(4, 5)
        assert self.r1.bottomleft == Point(0, 0)
        assert self.r1.bottomright == Point(4, 0)
        assert self.r1.center == Point(2, 2.5)

    def test_area(self):
        assert self.r1.area() == 20
        assert self.r3.area() == 24
        assert self.r4.area() == 2

    def test_move(self):
        self.r4.move(2, 3)
        assert self.r4.bottomleft == Point(3, 4)
        assert self.r4.topright == Point(5, 5)
        przed = self.r1.center
        self.r1.move(0, 0)
        assert self.r1.center == przed

    def test_intersection(self):
        przeciecie = self.r1.intersection(self.r3)
        assert przeciecie.bottomleft == Point(0, 0)
        assert przeciecie.topright == Point(2, 3)
        assert self.r1.intersection(Rectangle(10,10,12,12)) is None

    def test_cover(self):
        pokrycie = self.r1.cover(self.r3)
        assert pokrycie.bottomleft == Point(-2, -3)
        assert pokrycie.topright == Point(4, 5)

    def test_make4(self):
        czesci1 = self.r1.make4()
        assert len(czesci1) == 4

        for p in czesci1:
            assert self.r1.left <= p.left < p.right <= self.r1.right
            assert self.r1.bottom <= p.bottom < p.top <= self.r1.top

        calosc = sum(p.area() for p in czesci1)
        assert calosc == self.r1.area()

        czesci2 = self.r3.make4()
        assert czesci2[0].bottomleft == self.r3.bottomleft
        assert czesci2[3].topright == self.r3.topright

    def teardown_method(self):
        del self.r1
        del self.r2
        del self.r3
        del self.r4