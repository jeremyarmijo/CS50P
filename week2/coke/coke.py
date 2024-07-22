try:
    due = 50
    while due > 0:
        print("Amount Due: %d" % due)
        coin_use = int(input("Insert Coin: "))
        if coin_use == 50 or coin_use == 25 or coin_use == 10 or coin_use == 5:
            due -= coin_use
    if due < 0:
        due *= -1
    print("Change Owed: %d" % due)
except:
    exit(-1)