import sys
import emoji

try:
    string = input("Input: ")
    print(emoji.emojize("Output: " + string, language="alias"))
except:
    exit(1)