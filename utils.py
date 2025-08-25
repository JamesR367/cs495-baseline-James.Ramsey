def AlternatingLetters(s):
    s = s.lower()
    counter = 0
    phrase= ""
    while counter < len(s):
        if counter % 2 == 0:
            phrase += s[counter].upper()
        else:
            phrase += s[counter]
        counter+=1
    return phrase



