def findWord(jumble, list):
    '''Returns a list of words with all of the same letters as the original word'''
    newList = []
    for word in list:
        if len(jumble) != len(word):
            continue
        isOK = False  # Did the current word pass the test?
        for letter in jumble:
            if not jumble.count(letter) == word.count(letter):
                break
            if letter == jumble[len(jumble)-1]:
                isOK = True
        if isOK == True:
            newList.append(word)
        isOK = False
    return newList
