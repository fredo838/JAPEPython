from random_words import RandomWords
import urllib.request
import json
from thesaurus import Word


class Joke(object):

    def __init__(self, type_name, word_types, word_requirements):
        self.type_name = type_name
        self.word_types = word_types
        self.word_requirements = word_requirements
        self.words = [None, None, None, None]

    def build(self):
        raise NotImplementedError("You should implement this feature")


class BazaarJoke(Joke):

    def __init__(self, type_name="Bazaar", word_types=None, word_requirements=None):
        if word_requirements is None:
            word_requirements = ["hom 3 4", "syn 1 3", "syn 2 4"]
        if word_types is None:
            word_types = ["adjective", "noun", "adjective", "noun"]
        super(BazaarJoke, self).__init__(type_name, word_types, word_requirements)

    def build(self):
        """
        Returns a joke in Bazaar form, using 2 adjectives and 2 nouns.
        :return:
        """
        while self.words[0] is None and self.words[1] is None:
            self.words[2], self.words[3] = get_homonyms("adj")
            try:
                self.words[0] = Word(self.words[2]).synonyms(partOfSpeech=["adj"])[0]
            except:
                self.words[0] = None
                self.words[1] = None
                continue
            try:
                self.words[1] = Word(self.words[3]).synonyms(partOfSpeech=["noun"])[0]
            except:
                self.words[0] = None
                self.words[1] = None
                continue
        return "What do you call a(n) " + self.words[0] + " " + self.words[1] + "? A(n) " + self.words[2] + " " + self.words[3] + "."


class BazaarAltJoke(Joke):

    def __init__(self, type_name="BazaarAlt", word_types=None, word_requirements=None):
        super(BazaarAltJoke, self).__init__(type_name, word_types, word_requirements)

    def build(self):
        """
        Returns a joke in an alternate Bazaar form, using 4 nouns.
        :return:
        """
        while self.words[0] is None and self.words[1] is None:
            self.words[2], self.words[3] = get_homonyms("n")
            try:
                self.words[0] = Word(self.words[2]).synonyms(partOfSpeech=["noun"])[0]
            except:
                self.words[0] = None
                self.words[1] = None
                continue
            try:
                self.words[1] = Word(self.words[3]).synonyms(partOfSpeech=["noun"])[0]
            except:
                self.words[0] = None
                self.words[1] = None
                continue
        return "When is a(n) " + self.words[0] + " like a(n) " + self.words[1] + "? When it is a(n) " + self.words[3] + ". (" + self.words[2] + ")"


class VNAlt(Joke):

    def __init__(self):
        super(VNAlt, self).__init__("VNAlt", None, None)

    def build(self):
        """
        Returns a joke in an allternate VN form of Jape. Uses two verbs and two nouns.
        :return:
        """
        while self.words[0] is None and self.words[1] is None:
            self.words[2], self.words[3] = get_homonyms("v")
            try:
                self.words[0] = Word(self.words[2]).synonyms(partOfSpeech=["verb"])[0]
            except:
                self.words[0] = None
                self.words[1] = None
                continue
            try:
                self.words[1] = Word(self.words[3]).synonyms(partOfSpeech=["noun"])[0]
            except:
                self.words[0] = None
                self.words[1] = None
                continue
        return "Why did someone " + self.words[0] + " a(n) " + self.words[1] + "? So they could " + self.words[2] + " the " + self.words[3]


def get_synonym(word, part_of_speech=None):
    """
    Returns a synonym for a given word.
    :param word:
    :param part_of_speech:
    :return:
    """
    if part_of_speech:
        return Word(word).synonyms(partOfSpeech=part_of_speech)[0]
    else:
        return Word(word).synonyms()


def get_homonyms(second_type):
    """
    Returns two random homonyms
    :param second_type:
    :return:
    """
    while True:
        word = RandomWords().random_word()
        response = urllib.request.urlopen('https://api.datamuse.com/words?md=p&rel_rhy=' + word)
        html = json.loads(response.read())
        if html == "[]":
            continue
        else:
            for entry in html:
                if 'tags' in entry and entry['tags'] == [second_type]:
                    return entry['word'], word
                else:
                    continue


if __name__ == "__main__":
    print(BazaarJoke().build())
    print(BazaarAltJoke().build())
    print(VNAlt().build())
