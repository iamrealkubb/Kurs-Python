from points import Point

class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 <= x2:
            min_x, max_x = x1, x2
        else:
            min_x, max_x = x2, x1

        if y1 <= y2:
            min_y, max_y = y1, y2
        else:
            min_y, max_y = y2, y1

        self.pt1 = Point(min_x, min_y)
        self.pt2 = Point(max_x, max_y)

    def from_points(punkty):
        if isinstance(punkty, tuple):
            punkty = list(punkty)
        if len(punkty) != 2:
            raise ValueError("potrzebne dokladnie dwa punkty!")
        p1, p2 = punkty
        return Rectangle(p1.x, p1.y, p2.x, p2.y)

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

    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def right(self):
        return self.pt2.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def top(self):
        return self.pt2.y

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    @property
    def center(self):
        return Point((self.left + self.right) / 2, (self.bottom + self.top) / 2)

    def area(self):
        szerokosc = abs(self.pt2.x - self.pt1.x)
        wysokosc = abs(self.pt2.y - self.pt1.y)
        return szerokosc * wysokosc

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

    def intersection(self, other):
        if not isinstance(other, Rectangle):
            return None

        lewa = max(self.pt1.x, other.pt1.x)
        prawa = min(self.pt2.x, other.pt2.x)
        dolna = max(self.pt1.y, other.pt1.y)
        gorna = min(self.pt2.y, other.pt2.y)

        if lewa >= prawa or dolna >= gorna:
            return None

        return Rectangle(lewa, dolna, prawa, gorna)
    
    def cover(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("cover oczekuje Rectangle")

        min_x = min(self.pt1.x, other.pt1.x)
        max_x = max(self.pt2.x, other.pt2.x)
        min_y = min(self.pt1.y, other.pt1.y)
        max_y = max(self.pt2.y, other.pt2.y)

        return Rectangle(min_x, min_y, max_x, max_y)

    def make4(self):
        srodek_x = (self.pt1.x + self.pt2.x) / 2
        srodek_y = (self.pt1.y + self.pt2.y) / 2

        dol_lewo = Rectangle(self.pt1.x, self.pt1.y, srodek_x, srodek_y)
        dol_prawo = Rectangle(srodek_x, self.pt1.y, self.pt2.x, srodek_y)
        gora_lewo = Rectangle(self.pt1.x, srodek_y, srodek_x, self.pt2.y)
        gora_prawo = Rectangle(srodek_x, srodek_y, self.pt2.x, self.pt2.y)

        return (dol_lewo, dol_prawo, gora_lewo, gora_prawo)