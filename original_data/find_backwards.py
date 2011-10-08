#!/usr/bin/env python
# 2009-12-10
# For reversible recursive acronyms
# Find words that, when spelled backwards, make another word
# Words must have 'r' and 'b', just for fun

import cPickle as pickle

keys = pickle.load(open("words.pickle"))
words = []
matches = []
searched = 0

for w in open("dict"):
    words.append(w.strip())

for word in words:
    if word != word[::-1]:
        try:
            similar = keys["".join(sorted(list(word)))]
            for w in similar:
                if w == word[::-1]:
                    matches.append(word)
        except:
            pass
    searched += 1
    if searched % 1000 == 0:
        print searched, word

#print matches, len(matches)
for word in matches:
    if word.__contains__("r") and word.__contains__("b"):
        print "%s\t%s" % (word, word[::-1])
