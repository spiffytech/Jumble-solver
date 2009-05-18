import cPickle as pickle

from classes import Jumble, Word

def main():
    dictFile = file("words.pickle")
    dict = pickle.load(dictFile)
    jumbles = []
    for i in range(0, 7):  # Get jumbles from the user and process them
        j = Jumble()
        j.original = raw_input("Next jumbled word: ")
        if j.original == "":
            break
        positions = raw_input("Important positions in this word: ")
        j.positions = positions.split(",")
        for i in range(0, len(j.positions)):
            j.positions[i] = int(j.positions[i])
            j.positions[i] = j.positions[i]-1

        j.agrams = findWord(j.original, dict)
        jumbles.append(j)

#    for j in jumbles:
#        print j.agrams
    solve(jumbles, dict)



def solve(jumbles, dict):
    '''Takes the solved individual jumbles and solves the punchline'''
    freq = pickle.load(file("word_frequency.pickle"))
    jumble = Jumble()

    for j in jumbles:
        for a in j.agrams:
            for p in j.positions:
                jumble.original += a[p]

    jumble.agrams = findWord(jumble.original, dict)
    w = Word()
    print sorted(jumble.agrams, w.freq_compare).reverse()



def findWord(jumble, dict):
    '''Returns a list of anagrams of the jumbled word'''
    agrams = []
    for word in dict:
        isOK = False  # Did the current word pass the test?
        if len(jumble) != len(word):  # Only single words for now
            continue

        for letter in jumble:
            if not jumble.count(letter) == word.count(letter):
                break
            if letter == jumble[len(jumble)-1]:
                isOK = True

        if isOK == True:
            agrams.append(word)
        isOK = False

    return agrams



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
