# Complete the 'maximumOccurringCharacter' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts STRING text as parameter.
#

def maximumOccurringCharacter(text):
    # Write your code here
    dict1 = {}

    for i in text:
        if i in dict1:
            dict1[i] = dict1[i] + 1
        else:
            dict1[i] = 1

    print(dict1)

    s_dict = {}
    sorted_values = sorted(dict1.values(), reverse=True)

    for j in sorted_values:
        for k in dict1.keys():
            if dict1[k] == j:
                s_dict[k] = dict1[k]
                break
    print(s_dict)

    r = list(s_dict.keys())[0]
    return str(r)

print("Actual output: ", maximumOccurringCharacter("Hello World"))