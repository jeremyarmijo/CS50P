def main():
    try:
        data = input("Input: ")
        data = shorten(data)
        print("Output: %s" % data)
    except ValueError:
        exit(-1)

def shorten(data):
    to_delete = ["a", "e", "i", "o", "u"]
    for i in range(0, len(to_delete)):
        data = data.replace(to_delete[i], "")
        data = data.replace(to_delete[i].upper(), "")
    return data

if __name__ == "__main__":
    main()
