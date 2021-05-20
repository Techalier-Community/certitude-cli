from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import os
import platform 
from rich import print

def font_detail():
    print("\nEnter the font details:")
    fontfile = input("Font file name from the above list :")
    fontsize = int(input("Size of the font :"))
    fontdet = ImageFont.truetype(fontfile, fontsize)
    return fontdet

def font_color():
    fontcolor = input("\nEnter the colour of font in hexcode:")
    return fontcolor

def make_cert(name_l, img):
    fontdeta = font_detail()
    fontcolo = font_color()
    folder = input("\nEnter a name to make folder:")
    response = os.system("mkdir "+folder)
    WIDTH, HEIGHT = int(input("Enther the x coordinate to print name:")), int(input("Enter the y coordinate to print name:"))
    print("\nProcess Initiated\nProcessing....................................")
    for i in range(len(name_list)):
        save_cert(get_capitalized_name(name_list[i]), img, fontdeta, fontcolo, folder, WIDTH, HEIGHT)


def save_cert(name, image, fontd, fontc, foldername, w, h):
    image_source = Image.open(image) 
    draw = ImageDraw.Draw(image_source)
    name_width, name_height = draw.textsize(name, font=fontd)
    draw.text((w-name_width/2, h-name_height/2),
              name, fill=fontc, font=fontd)
    image_source.save("./"+foldername+"/" + name+".pdf")
    print('printing certificate of: '+name)

def get_capitalized_name(name):
    lst = name.split()
    capi_name = ' '.join([a.capitalize() for a in lst])
    return capi_name

if __name__ == '__main__':
    plt = platform.system()
    if plt == "Windows":
        response = os.system("cls")
    elif plt == "Linux":
        response = os.system("clear")
    elif plt == "Darwin":
        response = os.system("clear")
    else:
        os.system("clear")

    print("\nWelcome to the Certitude App!\n[link=http://certitude.community.techalier.com]CLI version 1.0.1[/link]\nAll the files required for this procedure should be in the same folder as this python app.\n\nDeveloped by Parjanya Modi & Sumedh D Karanth. Powered by [link=https://community.techalier.com]Techalier Community[/Link]")
    
    print("\nMenu\n1.Make Certificate on computer\n2.Exit the app")
    choice = int(input("\nEnter the choice:"))
    
    if choice == 1:
        print("\nList of files in your folder:\n")
        if plt == "Windows":
            response = os.system("dir")
        elif plt == "Linux":
            response = os.system("ls")
        elif plt == "Darwin":
            response = os.system("ls")
        else:
            response = os.system("ls")
        print(response)
        certemp = input("\nEnter the certificate template name from above mentioned list: ")
        excname = input("Enter the name of Excel Sheet from above mentioned list: ")
        form = pd.read_excel(excname)
        name_list = form['Name'].to_list()
        make_cert(name_list, certemp)
        
    if choice == 2:
        print("\n\nThanks for using this app!\n\n")
        exit(0)