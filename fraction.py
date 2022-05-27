

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        result_num = self.numerator * other.denominator + other.numerator * self.denominator
        result_denom = self.denominator * other.denominator
        print(type(result_num))
        return Fraction(result_num, result_denom)


    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

if __name__ == '__main__': #if fraction.py will be imported as a module this will not run
    example = Fraction(1, 2)
    example2 = Fraction(1, 3)
    print(example) #thanks to __str__ magic method!
    print(example + example2)
