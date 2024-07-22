def find_extension(string, extension, path):
    string = string.lower()
    if string.find(extension) != -1:
        if extension == ".jpg":
            extension = ".jpeg"
        if extension == ".txt":
            extension = ""
        print(path + extension.replace(".", ""))
        return 0
    return -1

try:
    string = input("File name: ")
    if find_extension(string, ".gif", "image/") == 0:
        exit(0)
    if find_extension(string, ".jpeg", "image/") == 0:
        exit(0)
    if find_extension(string, ".jpg", "image/") == 0:
        exit(0)
    if find_extension(string, ".png", "image/") == 0:
        exit(0)
    if find_extension(string, ".pdf", "application/") == 0:
        exit(0)
    if find_extension(string, ".txt", "text/plain") == 0:
        exit(0)
    if find_extension(string, ".zip", "application/") == 0:
        exit(0)
    print("application/octet-stream")
except:
    exit(1)