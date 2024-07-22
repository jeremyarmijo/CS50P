import sys

def main():
    print(convert(input("Hours: ")))

def check_format(s):
    in_format = ["AM", "PM"]
    if len(s) != 5:
        return False
    if s[1] not in in_format or s[4] not in in_format:
        return False
    if s[2] != "to":
        return False
    return True

def minutes_precision(true_hour, hour, horaire):
    true_hour = hour.split(":")
    if int(true_hour[0]) > 12 or int(true_hour[0]) < 0:
        true_hour = "error"
    if int(true_hour[1]) > 59 or int(true_hour[1]) < 0:
        true_hour = "error"
    if horaire == "PM":
        true_hour[0] = str(int(true_hour[0]) + 12)
        if int(true_hour[0]) == 24:
            true_hour[0] = "12"
    else:
        if int(true_hour[0]) == 12:
            true_hour[0] = "0"
    if int(true_hour[0]) < 10:
        true_hour[0] = str("0" + true_hour[0])
    return true_hour

def final_hour(hour, horaire):
    true_hour = hour
    if true_hour.find(":") == -1:
        if int(true_hour) < 10:
            true_hour = str("0" + true_hour)
        if horaire == "PM":
            true_hour = str(int(true_hour) + 12)
            if int(true_hour) == 24:
                true_hour = "12"
        else:
            if int(true_hour) == 12:
                true_hour = "00"
        return true_hour + ":00"
    true_hour = minutes_precision(true_hour, hour, horaire)
    return true_hour[0] + ":" + true_hour[1]

def format_hour(my_list):
    hour = []
    hour.append(final_hour(my_list[0], my_list[1]))
    hour.append(final_hour(my_list[3], my_list[4]))
    return hour

def convert(s):
    my_list = s.split(" ")
    correct_format = check_format(my_list)
    if correct_format == False:
        sys.exit("ValueError")
    hour = format_hour(my_list)
    if "error" in hour:
        sys.exit("ValueError")
    return str(hour[0] + " to " + hour[1])

if __name__ == "__main__":
    main()