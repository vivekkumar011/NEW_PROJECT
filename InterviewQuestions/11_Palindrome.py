#num = int(input("Enter number = "))

num = 1123211
n = num
rem = 0

while num>0:
    last_dig = num%10
    rem = rem * 10 + last_dig
    num=int (num/10)

print(rem)

if n == rem:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")