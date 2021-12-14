# A program to help solve Ch 17, problem number 5: finding zeros of polynomial rings.

def modular(value, modulus):
    value = value % modulus
    return value

def y_b(x):
    x = x % 5
    y1 = 3*x*x*x-4*x*x-x+4
    return modular(y1, 5)

def y_a(x):
    x = x % 12
    y1 = 5*x*x*x+4*x*x-x+9
    return modular(y1, 12)

lower = int(input("Enter the lower bound value: "))
upper = int(input("Enter the upper bound value: "))

for i in range(lower, upper):
    print(f"y({i}) = {y_a(i)}")

    if y_a(i) == 0:
        print(f"Zero found at x = {i}")
    elif i == upper and y_a(i) != 0:
        print("No zeros found in the specified range")

#def gen_equiv_class(value, modulus, l_bound, u_bound):

#number = int(input("Enter the value: "))
#print(f"y_a({number}) = {y_a(number)}")

#modulus = int(input("Enter the modulus: "))
#print(f"The number {number} mod {modulus} is: {modular(number, modulus)}")