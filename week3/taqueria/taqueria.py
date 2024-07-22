dictionary = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

def main():
    total = 0
    while 1:
        try:
            string = str(input("Item: ").lower())
            if string in dictionary:
                total = total + float(dictionary[string])
                print("Total: $%.2f" % float(total))
        except EOFError:
            exit(0)
        except ValueError:
            pass

if __name__ == "__main__":
    main()