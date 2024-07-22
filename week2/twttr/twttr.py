try:
    to_delete = ["a", "e", "i", "o", "u"]
    data = input("Input: ")
    for i in range(0, len(to_delete)):
        data = data.replace(to_delete[i], "")
        data = data.replace(to_delete[i].upper(), "")
    print("Output: %s" % data)
except:
    exit(-1)