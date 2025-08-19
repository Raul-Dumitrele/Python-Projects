from PIL import Image
def asciiConvert(image,type,saveas,scale):
    scale=int(scale)
    
    #Open and get image size
    img=Image.open(image)
    w,h=img.size
    
    #resize image(downscale)
    img.resize((w//scale, h//scale)).save("resized.%s" % type)

    
    #open new image
    img=Image.open("resized.%s"%type)
    w,h=img.size    #get new width and height
    
    #list wist correct lenght and height(same as resized image)
    grid=[]
    for i in range(h):
        grid.append(["X"]*w)
    
    pix=img.load()
    
    
    for y in range(h):
        for x in range(w):
            brightness = sum(pix[x, y])
            if brightness == 0:
                grid[y][x] = "#"
            elif brightness in range(1, 100):
                grid[y][x] = "X"
            elif brightness in range(100, 200):
                grid[y][x] = "%"
            elif brightness in range(200, 300):
                grid[y][x] = "&"
            elif brightness in range(300, 400):
                grid[y][x] = "*"
            elif brightness in range(400, 500):
                grid[y][x] = "+"
            elif brightness in range(500, 600):
                grid[y][x] = "/"
            elif brightness in range(600, 700):
                grid[y][x] = "("
            elif brightness in range(700, 750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
                
                
    art=open(saveas,"w")

    for row in grid:
        art.write("".join(row)+"\n")

    art.close()
    
if __name__ == '__main__':
    asciiConvert("x5.png","png","x5.txt","3")









