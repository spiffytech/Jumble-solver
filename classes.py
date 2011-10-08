import cPickle as pickle

class Jumble:
    def __init__(self, original=""):
        self.original = original
        self.agrams = []
        self.positions = []

class Word:
    def __init__(self, word=None, frequency=None, partOfSpeech=None):
        self.freq = pickle.load(file("word_frequency.pickle"))
        self.word = word
        self.frequency = frequency
        self.partOfSpeech = partOfSpeech

    def freq_compare(self, x, y):
        keys = self.freq.keys()
        if not x in keys:
            return -1
        elif not y in keys:
            return 1
        elif self.freq[x] > self.freq[y]:
            return 1
        elif self.freq[x] < self.freq[y]:
            return -1
        else:
            return 0
