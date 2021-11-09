def oldmacdonald(text):
    firstletter = text[0]
    inbetween = text[1:3]
    fourthletter = text[3]
    remaining = text[4:]
    print(firstletter.capitalize()+inbetween+fourthletter.capitalize()+remaining)

oldmacdonald('macdonald')