from PIL import Image
import tkinter as tk
from tkinter import filedialog

# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
# ASCII_CHARS = ["@@", "##", "SS", "%%", "??", "**", "++", ";;", "::", ",,", ".."]

# ASCII_CHARS = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# resize image according to a new width
def resize_image(image, new_width=100):
    #resize image, but make its widt a bit wider
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)


# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)


# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return (characters)


def main(path, new_width=100):
    # Create the file selection dialog
    root = tk.Tk()
    root.withdraw()

    # path = filedialog.askopenfilename()
    #get image name
    name = path.split("\\")[-1]
    print(name)
#open jpeg image
    try:
        image = Image.open(path)
    except:
        print(path, " is not a valid pathname to an image.")
        return

    # convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)] for index in range(0, pixel_count, new_width)])

    # print result
    print(ascii_image)

    # save result to "ascii_image.txt"
    # save_to_file("ascii_image.txt", ascii_image)
    save_to_file("C:\\Users\\Isi\\OneDrive\\Desktop\\Media\\Pic\\Nazi\\ASCII"+name+".txt", ascii_image)

def save_to_file(path, ascii_image):
    with open(path, "w") as f:
        f.write(ascii_image)

# run program
# main()

import glob
#get path with \ and /
path = "C:\\Users\\Isi\\OneDrive\\Desktop\\Media\\Pic\\Nazi"
# Get a list of all the JPG and PNG images in the "images" directory
image_list = glob.glob("C:\\Users\\Isi\\OneDrive\\Desktop\\Media\\Pic\\Nazi\\*.jpg") + glob.glob("C:\\Users\\Isi\\OneDrive\\Desktop\\Media\\Pic\\Nazi\\*.jpeg")
# Loop through each image in the image_list, and for each image:
for file_name in image_list:
    # Run the main() function
    main(file_name)
