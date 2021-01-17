for _ in range(5):
    for i in range(_):
        print ("*", end='')
    print(end="\n")

for _ in range(5):
    for i in range(5,_, -1):
        print("*", end='')
    print(end="\n")
