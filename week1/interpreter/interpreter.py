str = input("Expression: ");
words = str.split(" ");

if len(words) != 3:
    exit(-1)
if words[1] == "+":
    print(float(float(words[0]) + float(words[2])))
if words[1] == "-":
    print(float(float(words[0]) - float(words[2])))
if words[1] == "*":
    print(float(float(words[0]) * float(words[2])))
if words[1] == "/":
    if words[2] == "0":
        exit(-1)
    print(float(float(words[0]) / float(words[2])))
