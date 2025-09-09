import os
from PIL import Image

def watermark_photo(input_image_path,watermark_image_path,output_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert("RGBA")
    # add watermark to your image
    position = base_image.size
    newsize = (int(position[0]*8/100),int(position[0]*8/100))                   #The watermark resizes to 8% of the photo width (in both directions → square).
    watermark = watermark.resize(newsize)

    new_position = position[0]-newsize[0]-20,position[1]-newsize[1]-20          #Watermark positioning (bottom right with 20px margin)
    transparent = Image.new(mode='RGBA',size=position,color=(0,0,0,0))          #Create a new transparent empty image
    transparent.paste(base_image,(0,0))                                         #Paste the original image
    transparent.paste(watermark,new_position,watermark)                         #Paste the watermark image
    image_mode = base_image.mode
    print(image_mode)
    if image_mode == 'RGB':                                                     #If the original image is RGB → save as RGB.
        transparent = transparent.convert(image_mode)
    else:
        transparent = transparent.convert('P')                                  #Otherwise convert it to "P" mode (paletted image, like GIF or PNG with color index).
    transparent.save(output_image_path,optimize=True,quality=100)               #Save in output_image_path with maximum quality.
    print("Saving"+output_image_path+"...")

folder = input("Enter Folder Path:")
watermark = input("Enter Watermark Path:")
os.chdir(folder)
files = os.listdir(os.getcwd())
print(files)
""" It asks for the folder with the pictures and the path of the watermark.
    It moves to that folder (chdir).
    It lists all the files."""

if not os.path.isdir("output"):                                                 #If output does not already exist, it creates it.
    os.mkdir("output")

c = 1
for f in files:
    if os.path.isfile(os.path.abspath(f)):
        if f.endswith(".png") or f.endswith(".jpg"):                           #If it's a file (isfile) and has the extension .png or .jpg → apply a watermark to it and save it in output/ with the same name.
            watermark_photo(f,watermark,"output/"+f)