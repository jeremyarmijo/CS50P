import re

def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    s = s.replace(",", " ").replace("?", " ").replace(".", " ")
    occurrence = len(re.findall(r"\bum\b", s, re.IGNORECASE))
    if occurrence == -1:
        occurrence = 0
    return occurrence

if __name__ == "__main__":
    main()
