import inflect

def main():
    list_name = []
    p = inflect.engine()
    while 1:
        try:
            name = str(input())
            list_name.insert(len(list_name), name)
        except EOFError:
            print(f"Adieu, adieu, to {p.join(list_name)}")
            exit(0)

if __name__ == "__main__":
    main()