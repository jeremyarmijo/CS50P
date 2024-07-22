from PIL import Image, ImageOps
import sys
import os

def error_handling():
    extensions = [".png", ".jpg", '.jpeg']
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if os.path.exists(sys.argv[1]) == True:
        file_name, file_extension = os.path.splitext(sys.argv[1])
        file_name, file_extension2 = os.path.splitext(sys.argv[2])
        if file_extension in extensions and file_extension2 in extensions:
            if file_extension != file_extension2:
                sys.exit("Input and output have different extensions")
    else:
        sys.exit("Input does not exist")

def main():
    error_handling()
    picture = Image.open(sys.argv[1])
    picture2 = Image.open("shirt.png")
    size = picture2.size
    picture = ImageOps.fit(picture, size)
    picture.paste(picture2, picture2)
    picture.save(sys.argv[2])

if __name__ == "__main__":
    main()