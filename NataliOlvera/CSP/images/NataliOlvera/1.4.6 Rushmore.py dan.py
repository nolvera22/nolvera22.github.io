import os.path
import matplotlib.pyplot as plt
import numpy as np
import PIL
import PIL.ImageDraw

def openfile(filename):
    directory = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(directory, filename)
    return PIL.Image.open(filename)

def cropimg(image):
    return image.crop((127,2,252,166))
  
def ovalmask(image):
    width = image.size[0]
    length = image.size[1]
    my_mask = PIL.Image.new('RGBA', (width, length), (0, 0, 0, 0))
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
          
dan = makegray(ovalmask(cropimg(openfile("Beyoce.JPG"))))
scott = makegray(ovalmask(cropimg(openfile("scott.JPG"))))
rush = openfile("Balloon.jpg")
dansmall = dan.resize((45,55)) #resizes dan
scottsmall = scott.resize((82, 130))




image = openfile("Beyonce.JPG")
image2 = openfile("Balloon.JPG")

fig, ax = plt.subplots(1, 4)
ax[0].imshow(image, interpolation='none')
ax[1].imshow(image2, interpolation='none')
ax[2].imshow(dansmall, interpolation='none')
ax[3].imshow(scottsmall, interpolation='none')
ax[4].imshow(rush, interpolation='none')
dansmall.save("CSP_dan.bmp")
scottsmall.save("CSP_scott.bmp")
rush.save("CSP_Rushmore.bmp")

fig.show()