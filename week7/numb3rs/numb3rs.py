import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    ipv4_regex = re.compile(r'(?:[0-9]{1,3}\.){3}[0-9]{1,3}$')
    my_bool = bool(ipv4_regex.match(ip))
    try:
        if my_bool == True:
            ip = ip.split(".")
            for i in range(0, len(ip)):
                if int(ip[i]) > 255:
                    return False
    except:
        return False
    return my_bool


...


if __name__ == "__main__":
    main()