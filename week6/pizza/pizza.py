import sys
import os
import tabulate

def error_handling():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if os.path.exists(sys.argv[1]) == True:
        file_name, file_extension = os.path.splitext(sys.argv[1])
        if file_extension != ".csv":
            sys.exit("Not a CSV file")
    else:
        sys.exit("File does not exist")

def file_body(file):
    copy = list(file.copy())
    copy.remove(copy[0])
    for i in range(0, len(copy)):
        copy[i] = copy[i].split(",")
    return copy

def main():
    error_handling()
    file = []
    with open(sys.argv[1], "r") as file_content:
        for line in file_content:
            file.append(line.replace("\n", ""))
    if len(file) > 1:
        copy_file = file_body(file)
        print(tabulate.tabulate(copy_file, list(file[0].split(",")), tablefmt="grid"))

if __name__ == "__main__":
    main()