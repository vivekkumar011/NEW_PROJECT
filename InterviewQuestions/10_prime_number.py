count =0

def p_num(n):
    global count
    for i in range(1,n+1):
        if n%i==0:
            count = count+1
    if count==2:
        print("Number {} is prime".format(n))
    else:
        print("Number {} is not prime".format(n))

p_num(31)

