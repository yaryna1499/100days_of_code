class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        result_num = self.numerator * other.denominator + other.numerator * self.denominator
        result_denom = self.denominator * other.denominator
        # print(type(result_num))
        return Fraction(result_num, result_denom)

    def __sub__(self, other):
        result_num = self.numerator * other.denominator - other.numerator * self.denominator
        result_denom = self.denominator * other.denominator
        # print(type(result_num))
        return Fraction(result_num, result_denom)

    def __mul__(self, other):
        result_num = self.numerator * other.numerator
        result_denom = self.denominator * other.denominator
        # print(type(result_num))
        return Fraction(result_num, result_denom)

    def __truediv__(self, other):
        return Fraction(self.numerator, self.denominator).__mul__(Fraction(other.denominator, other.numerator))

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)


if __name__ == '__main__':  # if fraction.py will be imported as a module this will not run
    example = Fraction(3, 2)
    example2 = Fraction(1, 3)
    print(example)  # thanks to __str__ magic method!
    print(example + example2)  # add operation test
    print(example - example2)  # substract operation test
    print(example * example2)  # multiplication test
    print(example / example2)  # division test
