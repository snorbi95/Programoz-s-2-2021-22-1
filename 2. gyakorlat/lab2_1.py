class Number:

    def __init__(self, num):
        self.n = num

    def square(self):
        return self.n ** 2

    def pow_k(self, k):
        return self.n ** k

    def absolute_value(self):
        if self.n >= 0:
            return self.n
        else:
            return -self.n

number1 = Number(-5)
print(number1.n)
print(number1.pow_k(3))
print(number1.absolute_value())
