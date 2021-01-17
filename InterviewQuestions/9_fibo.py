num = int(input("Enter"))

a=0
b=1
print(a)

count =0

while count<num-1:      #num-1 is because first num is a which we have already printed
    count = count +1
    print(b)
    c = a+b
    a=b
    b=c

