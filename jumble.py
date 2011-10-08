import cPickle as pickle

from classes import Jumble, Word

def main():
    dictFile = file("words.pickle")
    dict = pickle.load(dictFile)
    jumbles = []
    i = 0
    while 1:  # Get jumbles from the user and process them
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
        i+=1

    solve(jumbles, dict)



def solve(jumbles, dict):
    '''Takes the solved individual jumbles and solves the punchline'''
    freq = pickle.load(file("word_frequency.pickle"))
    jumble = Jumble()
    agrams = []

    # Isolate the important letters from the solved jumbles
    for j in jumbles:
        jumble.agrams = []
        for ana in j.agrams:
            for pos in j.positions:
                jumble.original += ana[pos]

    # Find anagrams of the final character set
        try:
            jumble.agrams += findWord(jumble.original, dict)
            print jumble.agrams
        except:
            pass



def findWord(jumble, dict):
    '''Returns a list of anagrams of the jumbled word'''
    agrams = []
#    print dict.keys()
    try:
        agrams = dict["".join(sorted(list(jumble)))]
    except:
        print "No such key: " + "".join(sorted(list(jumble)))
        agrams = None

    print agrams
    return agrams



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
