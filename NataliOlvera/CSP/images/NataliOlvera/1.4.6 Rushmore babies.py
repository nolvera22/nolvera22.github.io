import os.path
import matplotlib.pyplot as plt
import numpy as np
import PIL
import PIL.ImageDraw

def openfile(filename):
    directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(directory, filename)
    return PIL.Image.open(filename)

def cropimg1(image):
    return image.crop((171,60,300,278))
    
def cropimg2(image):
        return image.crop((150,50,240,160))
    
def cropimg3(image):
        return image.crop((10,51,215,332))

def ovalmask(image):
    width = image.size[0]
    length = image.size[1]
    my_mask = PIL.Image.new('RGBA', (width, length), (123, 0, 0, 0))
    drawing_layer = PIL.ImageDraw.Draw(my_mask)
    drawing_layer.ellipse((0, 0, width, length), fill=(255, 0, 0, 255))
    result = PIL.Image.new('RGBA', (width, length))
    result.paste(image, (0, 0), mask=my_mask)
    return result

def ovalmask(image1):
    width = image1.size[0]
    length = image1.size[1]
    my_mask = PIL.Image.new('RGBA', (width, length), (123, 0, 0, 0))
    drawing_layer = PIL.ImageDraw.Draw(my_mask)
    drawing_layer.ellipse((0, 0, width, length), fill=(255, 0, 0, 255))
    result = PIL.Image.new('RGBA', (width, length))
    result.paste(image1, (0, 0), mask=my_mask)
    return result

def ovalmask(image2):
    width = image2.size[0]
    length = image2.size[1]
    my_mask = PIL.Image.new('RGBA', (width, length), (123, 0, 0, 0))
    drawing_layer = PIL.ImageDraw.Draw(my_mask)
    drawing_layer.ellipse((0, 0, width, length), fill=(255, 0, 0, 255))
    result = PIL.Image.new('RGBA', (width, length))
    result.paste(image2, (0, 0), mask=my_mask)
    return result

def makegray(image):
    img2 = np.array(image)
    height = len(img2)
    width = len(img2[0])
    for row in range(height):
        for column in range (width):
            pxl = sum(img2[row][column][0:3])/3
        img2[row][column] = [pxl, pxl, pxl, img2[row][column][3]]
    image = PIL.Image.fromarray(img2)
    return image

def makegray(image):
    img2 = np.array(image)
    height = len(img2)
    width = len(img2[0])
    for row in range(height):
        for column in range (width):
            pxl = sum(img2[row][column][0:3])/3
        img2[row][column] = [pxl, pxl, pxl, img2[row][column][3]]
    image = PIL.Image.fromarray(img2)
    return image

dan = ovalmask(cropimg1(openfile("nicolas.JPG")))
kim = ovalmask(cropimg3(openfile("kim_K.JPG")))
Beyonce = ovalmask(cropimg2(openfile("Beyonce.JPG")))
rush = openfile("beach.jpg")
dansmall = dan.resize((31, 35))#resizes face
kimsmall = kim.resize((34, 38))
Beyoncesmall = Beyonce.resize((25, 31))
#scottsmall = scott.resize((82, 130))

rush.paste(dansmall, (98, 30), mask=dansmall)
rush.paste(kimsmall, (200, 30), mask=kimsmall)
rush.paste(Beyoncesmall, (155, 35), mask=Beyoncesmall)
#rush.paste(scottsmall, (379, 120), mask=scottsmall)

image = openfile("nicolas.JPG")
image2 = openfile("kim_K.JPG")
image1 = openfile("Beyonce.JPG")
image3 = openfile("beach.jpg")

#image2 = openfile("pretty_flower.JPG")

fig, ax = plt.subplots(1, 2)
ax[0].imshow(image3, interpolation='none')
ax[1].imshow(rush, interpolation='none')
#ax[1].imshow(dansmall, interpolation='none')

dansmall.save("CSP_nicolas_cage.bmp")
kimsmall.save("CSP_kim_K.bmp")
rush.save("CSP_beach.bmp")
Beyoncesmall.save("CSP_Beyonce.bmp")
fig.show()
  
