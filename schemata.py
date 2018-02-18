def indefinite_article(w):
    """Generate an indefinite article for the given phrase: a, an, or empty string"""
    if len(w) == 0:
        return ""
    if w.lower().startswith("a ") or w.lower().startswith("an ") or w.lower().startswith("the "):
        return ""
    return "an " if w.lower()[0] in list('aeiou') else "a "


def camel(s):
    """Camel case the given string"""
    return s[0].upper() + s[1:]


def removeArticle(s):
    """Remove the article in the beginning of the given phrase"""
    if s.startswith("a "):
        return s[2:]
    elif s.startswith("an "):
        return s[3:]
    elif s.startswith("the "):
        return s[4:]
    return s


# w1 is an adjective and w2 is a noun.
# d1 is an adjective synonym for w1
# d2 is an noun synonym for w2
def N2A2_joke(d1, d2, w1, w2):
    return "What do you call " + indefinite_article(d1) + d1 + " " + removeArticle(d2) + "? " + \
        camel(indefinite_article(w1)) + w1 + " " + w2 + "."


def N2A2_req():
    return ["hom 1 2", "syn 3 1", "syn 4 2", "adjective noun adjective noun"]


# w1 and w2 are both nouns
# d1 is an noun synonym for w1
# d2 is an noun synonym for w2
def N4_joke(d1, d2, w1, w2):
    return "When is " + indefinite_article(d1) + d1 + " like " + indefinite_article(d2) + d2 + "? " + \
           "When it is " + indefinite_article(w2) + w2 + "."


# w1 is a verb and w2 is a noun
# d1 is an verb synonym for w1
# d2 is an noun synonym for w2
def N2V2_joke(d1, d2, w1, w2):
    return "Why did someone " + d2 + " " + indefinite_article(d1) + d1 + "? " + \
           "So they could " + w2 + " " + indefinite_article(w1) + w1 + "."


# both are nouns, but w1 has a synonym that's an adjective
def N3A_joke(d1, d2, w1, w2):
    return "What do you call " + indefinite_article(d1) + d1 + " " + d2 + "? " + \
           camel(indefinite_article(w2)) + w2 + "."


# adjective with noun synonym is homophones with a noun with a noun synonym
def N2AN_joke(d1, d2, w1, w2):
    return "When is " + indefinite_article(d1) + d1 + " like " + indefinite_article(d2) + d2 + "? " + \
           "When it is " + indefinite_article(w1) + w1 + " " + w2 + "."
