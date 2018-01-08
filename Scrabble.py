import re
import WordValidator
import WordGenerator

class InputValidator:
    def __init__(self):
        self.userInput()
        self.word_gen = WordGenerator.WordGenerator(self.letters)
        self.possible_words = self.word_gen.possible_words
        self.dictionary = WordValidator.WordValidator()
        self.realWords()

    def validate(self, letters):
        if not re.search(r"[^a-zA-Z\s,]", letters):
            match = re.findall(r"[a-zA-Z]", letters)
            if len(match) >= 2:
                return list((c.lower() for c in match))

    def userInput(self):
        while True:
            tiles = raw_input("Please enter your tiles.\n")
            cleantiles = self.validate(tiles)
            if not cleantiles == None:
                self.letters = cleantiles
                break
            else:
                print("Those tiles are not valid!")

    def realWords(self):
        newwords = []
        for word in self.possible_words:
            if self.dictionary.validWord(word[0]):
                newwords.append(word)
        self.real_words = self.word_gen.sortWords(newwords)

    def __str__(self):
        printer = ""
        for word in self.real_words:
            printer += word[0] + ", score = " + str(word[1]) + "\n"
        return printer


if __name__ == '__main__':
    I = InputValidator()
    print I
