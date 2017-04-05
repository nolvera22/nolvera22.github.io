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
    
def ovalmask(image):
    width = image.size[0]
    length = image.size[1]
    my_mask = PIL.Image.new('RGBA', (width, length), (0, 123, 255, 0))
    drawing_layer = PIL.ImageDraw.Draw(my_mask)
    drawing_layer.ellipse((0, 0, width, length), fill=(255, 0, 0, 255))
    result = PIL.Image.new('RGBA', (width, length))
    result.paste(image, (0, 0), mask=my_mask)
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
    
    height = len(img)
    width = len(img[0])
    for r in range(420,480):
        for c in range(138,160):
            if sum(img[r] [c])> 500:
                img[r] [c] = [0,150,255]

dan = ovalmask(cropimg1(openfile("model.PNG")))
rush = openfile("dogs.jpg")
dansmall = dan.resize((210, 95))#resizes face
#scottsmall = scott.resize((82, 130))

rush.paste(dansmall, (503, 117), mask=dansmall)
#rush.paste(scottsmall, (379, 120), mask=scottsmall)

image = openfile("model.PNG")
image3 = openfile("dogs.jpg")

#image2 = openfile("pretty_flower.JPG")

fig, ax = plt.subplots(1, 2)
ax[0].imshow(image3, interpolation='none')
ax[1].imshow(rush, interpolation='none')
#ax[1].imshow(dansmall, interpolation='none')

dansmall.save("CSP_model.bmp")
rush.save("CSP_dogs.bmp")
fig.show()
  
