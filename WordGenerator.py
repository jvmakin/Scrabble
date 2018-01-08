from itertools import combinations
from itertools import permutations

class WordGenerator:

    def __init__(self, user_letters):
        self.possibleWords(user_letters)

    def possibleWords(self, letters):
        test_words = []
        length = len(letters)
        for i in range(2, length+1):
            combos = list(combinations(letters, i))
            for array in combos:
                score = self.scoreWord(array)
                for p in permutations(array):
                    test_words.append([''.join(p), score])
        self.possible_words = test_words

    def scoreWord(self, word):
        tile_score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
        sum = 0
        for i in range(0, len(word)):
            sum += tile_score[word[i].lower()]
        return sum

    def sortWords(self, words):
        sorted_words = sorted(words, key=lambda tup: tup[1], reverse = True)
        return sorted_words
