import csv
from thesaurus import Word
from random import shuffle
import random
import numpy as np
import copy
from random_words import RandomWords
import wget
import urllib


class Driver:
    def __init__(self):
        self.muse = "https://www.datamuse.com/api/"
        self.related = "ml"
        self.rhymes = "rel_rhy"

    def read_homophones(self):
        with open('homophones.csv', 'rb') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            l = []
            for row in spamreader:
                l.append(row)
        return l

    def generate_rhyming(self, other):
        response = urllib.urlopen('https://api.datamuse.com/words?rel_rhy=' + other)
        html = response.read()
        l = html.split(',')
        rymes = []
        for i in l:
            if i[0] == "{":
                rymes.append(i.split(":")[1][1:-1])
        return rymes

    def generate_similars(self, other):
        pass

    def generate_synonyms(self, other):
        return Word(other).synonyms()

    def get_words(self, bi_cons, set_words):
        if not bi_cons:
            return True, set_words
        if all_none(set_words):
            rw = RandomWords()
            set_words[0] = rw.random_word()
        for c_bi_con in bi_cons:
            bi_con = c_bi_con.split()
            fi = int(bi_con[1]) - 1
            si = int(bi_con[2]) - 1
            if set_words[fi] is None and set_words[si] is None:
                pass
            elif (not set_words[fi] is None) and (not set_words[si] is None):
                return False, []
            else:
                if set_words[fi] is None:
                    res, set_words = self.handle_bi_con(c_bi_con, bi_cons, set_words, si, fi)
                    return True, set_words
                else:
                    res, set_words = self.handle_bi_con(c_bi_con, bi_cons, set_words, fi, si)
                    return True, set_words

    def handle_bi_con(self, c_bi_con, bi_cons, set_words, oi, i):
        other_word = set_words[oi]
        # handle synonyms
        if c_bi_con.split()[0] == "syn":
            syns = self.generate_synonyms(other_word)
            for syn in syns:
                if not syn in set_words:
                    set_words_new = copy.deepcopy(set_words)
                    set_words_new[i] = syn
                    bi_cons_next = filter(lambda x: x != c_bi_con, bi_cons)
                    res = self.get_words(bi_cons_next, set_words_new)
                    if res[0]:
                        return res
            return False, set_words
        # handle ryhming
        if c_bi_con.split()[0] == "rym":
            rymes = self.generate_rhyming(other_word)
            for syn in rymes:
                if not syn in set_words:
                    set_words_new = copy.deepcopy(set_words)
                    set_words_new[i] = syn
                    bi_cons_next = filter(lambda x: x != c_bi_con, bi_cons)
                    res = self.get_words(bi_cons_next, set_words_new)
                    if res[0]:
                        return res
            return False, set_words

    def get_speech(self, word):
        """ return a list of poss 'speeches' (noun, verb ...) """
        posses = ['verb', 'noun', 'adj', 'adv', 'as in', 'conjunction']
        speeches = []

        def get_all_synonyms(word1, speech1):
            for w in Word(word1).synonyms('all', partOfSpeech=speech1):
                if not w == []:
                    return w
            return []

        def empty_tree(input_list):
            # print(input_list)
            if type(input_list) == type([]):
                for l in input_list:
                    if not empty_tree(l):
                        return False
                return True
            else:
                return False

        for poss in posses:
            if not empty_tree(get_all_synonyms(word, poss)):
                speeches.append(poss)
        return speeches


def no_none(w):
    for e in w:
        if e == None:
            return False
    return True


def all_none(w):
    for e in w:
        if e != None:
            return False
    return True


driver = Driver()
words = driver.get_words(["rym 2 3", "syn 1 4", "syn 1 2"], [None, None, None, None])
speeches = []
for word in words[1]:
    speeches.append(driver.get_speech(word))
w = []

for word in words[1]:
    try:
        w.append(Word(word).origin().split()[0])
    except IndexError:
        w.append(word)
print(w, speeches)


def generate_riddle(words, speeches):
    tot = list(zip(words, speeches))
    shuffle(tot)
    for i in range(0, len(words)):
        if words[0] == "adj":
            res.append(" " + tot[i][0])
