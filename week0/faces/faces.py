import sys
import emoji

try:
    string = input()
    i = 0
    while (i < len(string)):
        if string[i] == ':':
            if string[i + 1] == ')':
                sys.stdout.write(emoji.emojize(':slightly_smiling_face:'))
                i = i + 2
            if string[i + 1] == '(':
                sys.stdout.write(emoji.emojize(':slightly_frowning_face:'))
                i = i + 2
        sys.stdout.write(string[i])
        i += 1
except:
    exit(1)