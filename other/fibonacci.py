# My stupid realization:
def fibonacci(n):
    a1 = 0
    a2 = 1
    lst = []
    if n == 0:
        return "error"
    elif n == 1:
        return a1
    elif n > 1:
        for i in range(n-2):
            lst.append(a1+a2)
            a1, a2 = a2, a1+a2
        return [0, 1]+lst

print(fibonacci(10))

# Using for loop
nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

# Using recursion
def FibRec(a):
    if a <= 1:

        return a

    else:

        return (FibRec(a - 1) + FibRec(a - 2))


aterms = int(input("Enter the terms? "))

if aterms <= 0:

    print("Please enter a positive integer")

else:

    print("Fibonacci sequence:")

    for z in range(aterms):
        print(FibRec(z))

