for _ in range(1,51):
    if _ % 3 == 0:
        print("abc")
    elif _ % 5 == 0:
        print("def")
    elif _ % 10 == 0:
        print("abcdef")
    else:
        print(_)