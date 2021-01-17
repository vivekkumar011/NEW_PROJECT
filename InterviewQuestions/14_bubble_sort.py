#Input : 50 20 6 103 67 2 9

li = [50, 20, 6, 103, 67, 2, 9]
n = len(li)

for i in range(0, n):
    for j in range(0, n -i - 1):
        if li[j]>li[j+1]:
            li[j], li [j+1] = li[j+1], li [j]

print(li)

li1 = ["50", "20", "6", "103", "67", "2", "9"]
li1.sort(key=int)
print ("List with sort method = ", li1)