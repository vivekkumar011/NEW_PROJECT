string = 'SELENIUM'
count = 0

def num_of_E(s):
    global count
    for _ in string:
        if _ == s:
            count = count + 1
    return count


print (num_of_E('E'))