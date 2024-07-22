try:
    string = input("Greeting: ")
    if string == "Hello" or string.find("Hello") != -1:
        print("$0")
        exit(0)
    elif string[0] == 'H' and string != "Hello":
        print("$20")
    else:
        print("$100")
except:
    exit(1)