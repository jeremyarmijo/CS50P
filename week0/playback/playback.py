try:
    string = input()
    for i in range (0, len(string)):
        if string[i] == ' ':
            string = string.replace(" ", "...")

    print(string)
except:
    exit(1)