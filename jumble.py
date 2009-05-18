import cPickle as pickle

def main():
    dictFile = file("words")
    dict = pickle.load(dictFile)
    jumbles = []
    for i in range(0, 5):
        j = raw_input("Next jumbled word: ")
        if j == "":
            break

        jumbles.append([])
        jumbles[i].append(j)
        jumbles[i].append(findWord(jumbles[i][0], dict))

    for word in jumbles:
        print word[1]


class jumble:
    original = ""
    agrams = []
    positions = []



def solve(jumbles):
    dictFile = file("words")
    dict = pickle.load(dictFile)

    words = []
    for j in jumbles:
        words.append()




def findWord(jumble, words):
    '''Returns a words of words with all of the same letters as the original word'''
    newwords = []
    for word in words:
        isOK = False  # Did the current word pass the test?
        if len(jumble) != len(word):  # Only single words for now
            continue

        for letter in jumble:
            if not jumble.count(letter) == word.count(letter):
                break
            if letter == jumble[len(jumble)-1]:
                isOK = True

        if isOK == True:
            newwords.append(word)
        isOK = False

    return newwords


if __name__ == "__main__":
    main()
