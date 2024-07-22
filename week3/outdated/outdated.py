list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


def verif_date(date):
    start = [2, 2, 1800]
    date_max = [30, 12, 1900]

    if len(date) > 3:
        return False
    for i in range(0, len(start)):
        if int(date[i]) > date_max[i]:
            return False
    for i in range(0, len(date)):
        if int(date[i]) < 10:
            date[i] = "0" + date[i]
    return True

def check_syntax(list, date):
    date_max = [30, 1900]
    if date[0] not in list:
        return False
    for i in range(1, len(date)):
        if int(date[i]) > date_max[i - 1]:
            return False
    return True

def date_format(list, date):
    month = 0
    for i in range(0, len(list)):
        if list[i] == date[0]:
            month = i
    date[0] = str(month + 1)
    for i in range(0, len(date) - 1):
        if int(date[i]) < 10:
            date[i] = "0" + date[i]

def main():
    while 1:
        date = str(input("Date: "))
        if "/" in date:
            date = date.replace(" ", "")
            date = date.split("/")
            try:
                if verif_date(date) == False:
                    continue
                print("%s-%s-%s" % (str(date[2]), str(date[0]), str(date[1])))
                exit(0)
            except ValueError:
                pass
        else:
            try:
                if "," not in date:
                    continue
                date = date.replace(",", "")
                date = date.split(" ")
                if check_syntax(list, date) == False:
                    continue
                date_format(list, date)
                print("%s-%s-%s" % (str(date[2]), str(date[0]), str(date[1])))
                exit(0)
            except ValueError:
                pass

if __name__ == "__main__":
    main()