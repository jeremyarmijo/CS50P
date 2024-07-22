from numb3rs import validate

def test_ip():
    assert validate("255.256.256.256") == False
    assert validate("1.1.1.1") == True
    assert validate("13324.1.1.1") == False
    assert validate("-14.1.1.1") == False
    assert validate("1.1.1.1.1") == False