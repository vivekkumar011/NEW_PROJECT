num = int(input("Enter number = "))
sum = 0

while num>0:
    last_dig = num%10
    sum = sum * 10 + last_dig
    num=int (num/10)

print(sum)