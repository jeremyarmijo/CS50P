import sys

def special_value(ultime_value, value, ref):
    if ultime_value == value:
        print(ref)
        exit(0)

def fraction(nb1, nb2):
    nb1 = int(nb1)
    nb2 = int(nb2)
    nb2 = float(100 / nb2)
    ultime_value = 0.5
    for i in range(0, nb1):
        ultime_value += nb2
    if ultime_value >= 99:
        ultime_value = 100
    if ultime_value <= 2:
        ultime_value = 0
    return int(ultime_value)

def main():
    while 1:
        try:
            nb1, nb2 = list(input("Fraction: ").split("/"))
            if int(nb1) > int(nb2):
                continue
            ultime_value = fraction(nb1, nb2)
            special_value(ultime_value, 100, "F")
            special_value(ultime_value, 0, "E")
            print(str(ultime_value) + "%")
            exit(0)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()