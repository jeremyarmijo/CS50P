import sys

try:
    mass = float(input("m: "))
    c = 3 * 10 ** 8
    Energy = int((mass/1000 * c ** 2))
    Energy *= 10 ** 3
    print("E: %d" % Energy)

except:
    exit(1)
