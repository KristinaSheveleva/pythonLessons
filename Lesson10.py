#1 import math

# def cans(height, width, cover):
#     number_of_cans = math.ceil((height *width) / cover)
#     print(f"You will need {number_of_cans} cans of paint")

# test_h = int(input()) # Height of wall (m)
# test_w = int(input()) # Width of wall (m)
# coverage = 5
# cans(height=test_h, width=test_w, cover=coverage)

def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number % i==0:
            is_prime=False
    if is_prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")

n = int(input()) # Check this number
prime_checker(number=n)
