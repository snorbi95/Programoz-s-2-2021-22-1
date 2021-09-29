class Polygon:

    sides = []

    def __init__(self, p1):
        self.n = p1

    def input_sides(self):
        for i in range(self.n):
            side = int(input(f"Kerem az {i + 1}. oldal hosszat: "))
            self.sides.append(side)

    def disp_sides(self):
        try:
            for i in range(self.n):
                print(f'Az {i + 1}. oldal hossza: {self.sides[i]}')
        except IndexError:
            print('Nincsenek oldalhosszok megadva! Kerem adja meg oket: ')
            self.input_sides()

class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)

    def get_area(self):
        s = self.get_perimeter() / 2
        res = s
        for i in range(self.n):
            res *= (s - self.sides[i])
        return res ** 0.5

    def get_perimeter(self):
        res = 0
        for i in range(self.n):
            res += self.sides[i]
        return res

    def triangle_check(self):
        a = self.sides[0]
        b = self.sides[1]
        c = self.sides[2]
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return False
        return True

    def input_sides(self):
        while True:
            super().input_sides()
            if self.triangle_check():
                break
            print('Nem szerkesztheto harmoszog!')
            self.sides.clear()

# pol1 = Polygon(5)
# pol1.disp_sides()
# pol1.disp_sides()

tri1 = Triangle()
tri1.input_sides()
tri1.disp_sides()
print(tri1.get_perimeter())
print(tri1.get_area())


