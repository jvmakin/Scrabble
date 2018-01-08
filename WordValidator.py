class WordValidator:
    def __init__(self):
        self.wordDictionary()

    def wordDictionary(self):
        words = {}
        for line in open("scrabblewords.txt"):
            word = line.strip()
            key = word[0:2].lower()
            if key in words.keys():
                words[key].append(word.lower())
            else:
                words[key] = [word.lower()]
        self.dictionary = words

    def validWord(self, word):
        if word[0:2] in self.dictionary.keys():
            return word in self.dictionary[word[0:2].lower()]
        else:
            return False
