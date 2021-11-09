def lesseroftwoevens(a, b):
    print(b%2)
    if a % 2 == b % 2 == 0:
        if a < b:
            print(a)
        else:
            print(b)
    else:
        if a > b:
            print(a)
        else:
            print(b)


lesseroftwoevens(6, 9)
