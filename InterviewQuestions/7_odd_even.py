# Write  a program to find a given number is even or odd without using modulus operator?

def is_even(n):
    if int(n/2)*2==n:
        return True
    else:
        return False

print(is_even(50))