def almostthere(n):
    x = abs(n-100)
    y = abs(n-200)
    if x<=10 or y <= 10:
        print("True")
    else:
        print("False")



almostthere(194)