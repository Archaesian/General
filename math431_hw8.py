# A program to help solve Ch 17, problem number 5: finding zeros of polynomial rings.

def modular(value, modulus):
    value = value % modulus
    return value

def y_a(x):
    x = x % 12
    y1 = 5*x*x*x+4*x*x-x+9
    return modular(y1, 12)

def y_b(x):
    x = x % 5
    y1 = 3*x*x*x-4*x*x-x+4
    return modular(y1, 5)

def y_c(x):
    x = x % 7
    y1 = 5*x*x*x*x + 2*x*x - 3
    return modular(y1, 7)
    
def y_d(x):
    x = x % 2
    y1 = x*x*x + x + 1
    return modular(y1, 2)

lower = int(input("Enter the lower bound value: "))
upper = int(input("Enter the upper bound value: "))

for i in range(lower, upper):
    print(f"y({i}) = {y_d(i)}")

    if y_d(i) == 0:
        print(f"Zero found at x = {i}")
    elif i == upper and y_d(i) != 0:
        print("No zeros found in the specified range")
