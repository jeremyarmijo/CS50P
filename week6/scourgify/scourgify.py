import csv
import sys
import os

def error_handling():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if os.path.exists(sys.argv[1]) != True:
        sys.exit("Could not read " + sys.argv[1])

def main():
    error_handling()
    file = open(sys.argv[1])
    final_file = open(sys.argv[2], "w", newline="")
    reader = csv.DictReader(file)
    writer = csv.DictWriter(final_file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in reader:
        last_name, first_name = row["name"].strip().split(", ")
        writer.writerow({"first": first_name, "last": last_name, "house": row["house"]})

if __name__ == "__main__":
    main()