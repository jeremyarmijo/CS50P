import random

def find_level():
    nb = 0
    while 1:
        try:
            nb = int(input("Level: "))
            if nb <= 0:
                continue
            return nb
        except ValueError:
            pass

def main():
    nb = find_level()
    rand = random.randint(1, nb)
    while 1:
        try:
            new_nb = int(input("Guess: "))
            if new_nb < rand:
                print("Too small!")
            elif new_nb > rand:
                print("Too large!")
            else:
                print("Just right!")
                break
        except:
            pass

if __name__ == "__main__":
    main()