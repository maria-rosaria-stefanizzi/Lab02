
class Dictionary:
    def __init__(self):
        self.dict = {}

    def addWord(self, alien_word, translations):
        if alien_word in self.dict:
            for t in translations:
                if t not in self.dict[alien_word]:
                    self.dict[alien_word].append(t)
        else:
            self.dict[alien_word] = list(translations)

    def translate(self, alien_word):
        return self.dict.get(alien_word, None)

    def translateWordWildCard(self, query):
        pass