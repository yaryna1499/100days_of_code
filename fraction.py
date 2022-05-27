##This is test for git!
#Test 2 for new_branch!

class Fraction:
    def __init__(self, numerator, denumerator):
        self.numerator = numerator
        self.denumerator = denumerator

    ###def __add__(self):
        ##return ##########


    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denumerator)

if __name__ == '__main__': #if fraction.py will be imported as a module this will not run
    example = Fraction(1,2)
    example2 = Fraction(1,3)
    print(example) #thanks to __str__ magic method!
