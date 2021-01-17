#Input : {4,5,6,-8,0,-6,7,-3,0,9,-5},
#Output: {0,0,4,5,6,-8,-6,7,-3,9,-5}
#li = [4,5,6,-8,0,-6,7,-3,0,9,-5]

'''
count = 0
for i in range(len(li)):
    if li[i] != 0:
        # here count is incremented
        li[count] = li[i]
        count += 1
print(li)

while count < len(li):
        li[count] = 0
        count += 1

print(li)
'''

#####################################
li1 = [4,5,6,-8,0,-6,7,-3,0,9,-5]
li2 = []
count = 0

for i in li1:
    if i == 0:
        li2.append(i)

for i in li1:
    if i != 0:
        li2.append(i)

print (li2)
