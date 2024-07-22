def main():
    fruits = [["apple", "130"], ["avocado", "50"], ["sweet cherries", "100"], ["tomato", ""], ["banana", "110"], ["kiwifruit", "90"], ["pear", "100"]]
    try:
        choose = str(input("Item: ").lower())
        for i in range(0, len(fruits)):
            if choose in fruits[i][0]:
                print(fruits[i][1])

    except:
        exit(-1)
if __name__ == "__main__":
    main()
