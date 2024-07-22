import sys
import os

def error_handling():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if os.path.exists(sys.argv[1]) == True:
        file_name, file_extension = os.path.splitext(sys.argv[1])
        if file_extension != ".py":
            sys.exit("Not a Python file")
    else:
        sys.exit("File does not exist")

def main():
    error_handling()
    file = []
    list_com = []
    with open(sys.argv[1], "r") as file_content:
        for line in file_content:
            file.append(line.replace("\n", "").replace(" ", ""))
    for i in range(0, len(file)):
        if len(file[i]) == 0 or file[i][0] == "#":
            list_com.append(i)
    print(len(file) - len(list_com))

if __name__ == "__main__":
    main()