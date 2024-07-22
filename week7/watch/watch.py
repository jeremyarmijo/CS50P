import re
import sys

def main():
    print(parse(input("HTML: ")))


def find_balise(s):
    if s.find("<iframe", 0, len("<iframe")) == -1 or s.find("</iframe>", len(s) - len("</iframe>"), len(s)) == -1:
        return False
    return True

def find_protocole(s):
    if s.find("http:") != -1:
        return "http:"
    elif s.find("https:") != -1:
        return "https:"
    return "error"

def find_link(s):
    if s.find("youtube.com") == -1:
        return "error"
    if s.find("www.") != -1:
        return "www.youtube.com"
    return "youtube.com"

def parse(s):
    if find_balise(s) == False:
        return None
    protocole = find_protocole(s)
    youtube_link = find_link(s)
    index = s.find("src=\"" + protocole + "//" + youtube_link +"/embed/")
    start_code = index + len("src=\"" + protocole + "//" + youtube_link +"/embed/")
    end_code = s.find("\"", start_code)
    if index == -1 or start_code == -1 or end_code == -1:
        return None
    return "https://youtu.be/" + s[start_code:end_code]

if __name__ == "__main__":
    main()
