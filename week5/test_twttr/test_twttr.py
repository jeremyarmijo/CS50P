from twttr import shorten
import os

def tests():
    assert os.path.exists("twttr.py") == True
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"
    assert shorten("PYTHON") == "PYTHN"