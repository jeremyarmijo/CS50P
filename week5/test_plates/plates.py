def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    num_pos = False
    if len(s) < 2 or len(s) > 6:
        return False
    for i in range(0, len(s)):
        if s[i] == "." or s[i] == " ":
            return False
        if i <= 1 and s[i].isalpha() == False:
            return False
        if s[i].isalpha() == False:
            if s[i] == "0" and num_pos == False:
                return False
            num_pos = True
        if num_pos == True and s[i].isalpha() == True:
            return False        
    return True

if __name__ == "__main__":
    main()