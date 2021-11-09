def animalcrackers(text):
    newtext = text.split(" ")
    print(newtext[0])
    print(newtext[0][0])
    print(newtext[1])
    print(newtext[1][0])
    if newtext[0][0]==newtext[1][0]:
        print("True")
        return True
    else:
        print("False")
        return False


animalcrackers("Levelheaded Llama")