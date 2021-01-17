def reverse(num):
    sum = 0
    while num>0:
        rem = num%10
        sum = sum * 10 + rem
        num = int (num/10)
    return sum

n = int(input("Enter number: "))
print (reverse(n))