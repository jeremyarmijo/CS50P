def main():
    time = input("What time is it? ")
    time = convert(time)
    verif_time(time, 7, "breakfast time")
    verif_time(time, 12, "lunch time")
    verif_time(time, 18, "dinner time")

def verif_time(time, ref, menu):
    if time >= ref and time <= (ref + 1):
        print(menu)

def convert(time):
    x, y = time.split(":")
    hr = float(x)
    mins = float(y) * 1 / 60
    return float(hr + mins)

if __name__ == "__main__":
    main()
