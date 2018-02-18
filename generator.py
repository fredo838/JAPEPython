import scraper
from schemata import *


def generate_joke(joke_type="N2A2"):
    if joke_type == "N2A2":
        return N2A2()
    elif joke_type == "N4":
        return N4()
    elif joke_type == "N2V2":
        return N2V2()
    elif joke_type == "N3A":
        return N3A()
    elif joke_type == "N2AN":
        return N2AN()


def N2A2():
    d1, d2, w1, w2 = N2A2_req()


def N4():
    d1, d2, w1, w2 = N4_req()


def N2V2():
    d1, d2, w1, w2 = N2V2_req()


def N3A():
    d1, d2, w1, w2 = N3A_req()


def N2AN():
    d1, d2, w1, w2 = N2AN_req()


def filter_f(x):
    if len(x) < 5:
        return False
    else:
        return x[-5:] == "_joke"


def handle_reqs(schemata_req, driver):
    results = [None, None, None, None]
    for req in schemata_req[:-1]:
        if req[:3] == "hom":
            a = req.split()[1:]
            nounity1 = schemata_req[-1].split()[int(a[0]) - 1]
            nounity2 = schemata_req[-1].split()[int(a[1]) - 1]
            b, _, c, _ = driver.get_specific_random_homophones(nounity1, nounity2)
            results[int(a[0]) - 1] = b
            results[int(a[1]) - 1] = c
        if req[:3] == "syn":
            a = req.split()[1:]
            if results[int(a[0]) - 1] is not None:
                syno = driver.get_synonym(results[int(a[0]) - 1])
                results[int(a[1]) - 1] = syno
            elif results[int(a[1]) - 1] is not None:
                syno = driver.get_synonym(results[int(a[1]) - 1])
                results[int(a[1]) - 1] = syno
            else:
                raise ValueError
    return results


driver = scraper.Driver()
# schemata_names = filter(filter_f, dir(schemata))
# schemata_name = schemata_names[random.randint(0,len(schemata_names))]
s_req = N2A2_req()
d1, d2, w1, w2 = handle_reqs(s_req, driver)
print(d1, d2, w1, w2)
