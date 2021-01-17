'''
Input: I love my Company
Output a: ynapmoC ym evol I
Output b: I LovE MY CompanY
'''

string = "I love my Company"

#print(string[::-1])
#print(string.title())

def capitalize_first_last_letters(str1):
    str1 = str1.title()
    print("Str1 with title() = ", str1)

    result = ""

    for word in str1.split():
        result = result + word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize_first_last_letters("python exercises practice solution"))
#print(capitalize_first_last_letters("w3resource"))
#print(capitalize_first_last_letters(string))