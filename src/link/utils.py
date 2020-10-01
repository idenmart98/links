import string
import random


def gen_link():
    link = ''
    for i in range(5):
        link = link+random.choice(string.ascii_letters)
    return link
