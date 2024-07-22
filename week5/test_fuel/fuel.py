def special_value(ultime_value, value, ref):
    if ultime_value == value:
        print(ref)
        exit(0)

def convert(string):
    try:
        my_list = string.split("/")
        nb1 = int(my_list[0])
        nb2 = int(my_list[1])
        if nb1 > nb2:
            raise ZeroDivisionError
        nb2 = float(100 / nb2)
        ultime_value = 0.5
        for i in range(0, nb1):
            ultime_value += nb2
        if ultime_value >= 99:
            ultime_value = 100
        if ultime_value <= 2:
            ultime_value = 0
        return int(ultime_value)
    except ValueError:
        return 1
    except ZeroDivisionError:
        return 1

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

def main():
    while 1:
        try:
            string = str(input("Fraction: "))
            ultime_value = convert(string)
            if ultime_value == 1:
                continue
            print(gauge(ultime_value))
            exit(0)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

if __name__ == "__main__":
    main()