try:
    string = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    try:
        if int(string) == 42:
            print("Yes")
        elif int(string) != 42:
            print("No")
    except:
        if string.lower() == "forty-two" or string.lower() == "forty two":
            print("Yes")
        else:
            print("No")
except:
    exit(1)
