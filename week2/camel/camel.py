try:
    string = input("camelCase: ")        
    string = string.replace("N", "_n")
    string = string.replace("F", "_f")
    print(string)
except:
    exit(1)