def paperdoll(text):
    newlist = [x*3 for x in text]
    print(('').join(newlist))

paperdoll("Hello")