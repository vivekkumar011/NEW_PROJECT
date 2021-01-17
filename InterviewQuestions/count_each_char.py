s = "Ahana cutest kid"

dict1 = {}

for i in s:
    if i == ' ':
        pass
    else:
        if i in dict1:
            dict1[i] = dict1[i]+1
        else:
            dict1[i] = 1

print(dict1)