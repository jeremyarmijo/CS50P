from bank import value
import os

def tests():
    assert os.path.exists("bank.py") == True
    assert value("Hello") == 0
    assert value(" Hello ") == 0
    assert value("Hello, Newman") == 0
