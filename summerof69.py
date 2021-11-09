def summerof69(numlist):
    total =0
    add = True
    for num in numlist:
        while add:
            if num!=6:
                total = total + num
                break
            else:
                add = False
                break
        while not add:
            if num!=9:
                break
            else:
                add = True
                break
    return total


print(summerof69([4,5,6,7,8,9]))