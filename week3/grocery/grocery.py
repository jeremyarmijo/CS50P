def exists_in_list(my_list, word):
    nb = 0
    index = 0
    for i in range(0, len(my_list)):
        if word in my_list[i]:
            index = i
            nb += 1
    return nb, index

def main():
    my_list = []
    nb_items = []
    while 1:
        try:
            my_bool = False
            word = str(input().upper())
            nb, index = exists_in_list(my_list, word)
            nb_items.insert(len(nb_items), 1)
            if nb != 0:
                nb_items[index] += 1
                continue
            my_list.insert(len(my_list), word)
        except EOFError:
            my_list.sort()
            for i in range(0, len(my_list)):
                print(nb_items[i], my_list[i])
            exit(0)
        except ValueError:
            pass

if __name__ == "__main__":
    main()