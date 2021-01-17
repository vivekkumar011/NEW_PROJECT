num = 153
n = num
sum=0

while num>0:
    rem = num%10
    cube = rem*rem*rem
    sum = sum + cube
    num = int(num/10)

print(sum)

if n==sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
