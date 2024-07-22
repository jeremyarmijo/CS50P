def main():
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

def value(greeting):
    greeting = greeting.replace(" ", "")
    if greeting == "hello":
        return 20
    if greeting[0] == 'h' and greeting != "hello":
        return 100
    return 0

if __name__ == "__main__":
    main()
