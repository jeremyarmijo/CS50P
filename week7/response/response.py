from validator_collection import checkers

try:
    my_str = str(input("What's your email address? "))
    is_valid = checkers.is_email(my_str)
    if is_valid == True:
        print("Valid")
    else:
        print("Invalid")
except:
    print("Invalid")