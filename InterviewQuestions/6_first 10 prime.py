def prime(n):
    p_count = 0
    for i in range (1,n+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count = count + 1
        if count == 2:
            print(i)
            p_count = p_count + 1
            if p_count == 10:
                quit()
prime(50)