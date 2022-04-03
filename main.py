from random import randrange
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def randFactorial():
    rand = randrange(10)
    return [rand, factorial(rand)]

rand = randFactorial()

print("the factorial of", rand[0], "is", rand[1])