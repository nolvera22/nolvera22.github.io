import os.path
import matplotlib.pyplot as plt
import numpy as np
import PIL
import PIL.ImageDraw

def openfile(filename):
    directory = os.path.dirname(os.path.abspath(__file__)) #from directory we call on the filename
    filename = os.path.join(directory, filename)
    return PIL.Image.open(filename) #returns image called on

def ovalmask(image): #ovalmask is applied to first image
    width = image.size[0] #width is equal to the image size on the first value (x)
    length = image.size[1]
    my_mask = PIL.Image.new('RGBA', (width, length), (0,0,0,0))
    drawing_layer = PIL.ImageDraw.Draw(my_mask)#
    drawing_layer.ellipse((175,300,520,890), fill=(255,0,0,255))
    result = PIL.Image.new('RGBA', (width, length))
    result.paste(image,(0,0), mask=my_mask)
    return result
    
khloe = openfile("khloe.jpg") #open original picture file (edits will be made on this file)
khloe2 = openfile("khloe.jpg") #open original picture file (edits will NOT be made on this file)

image = openfile("daisy.jpg") #opens trump file
daisy = ovalmask(openfile("daisy.jpg")) #applies ovalmask coded specifically for daisyfile
daisysmall = daisy.resize((30, 15)) #resizes daisy to 200 in width and 170 in length
khloe.paste(daisysmall, (215, 120), mask=daisysmall) #pastes daisy to coordinates (35, 190) on original daisy file
khloe.paste(daisysmall, (165, 117), mask=daisysmall) #pastes daisy to coordinates (35, 190) on original daisy file

fig, ax = plt.subplots(1, 4) #displays 2 subplots where images will be placed
ax[0].imshow(khloe2, interpolation='none') #on first subplot the unedited Khole2 file will appear
ax[1].imshow(khloe, interpolation='none') #on second subplot the final edited avocuddle file will appear
ax[2].imshow(image, interpolation='none') #on first subplot the unedited Khole2 file will appear
ax[3].imshow(daisy, interpolation='none') #on first subplot the unedited daisy2 file will appear

fig.show() #shows end product