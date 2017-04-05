import os.path
import matplotlib.pyplot as plt
import numpy as np
import PIL
import PIL.ImageDraw

# Open the image file
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'Beyonce.jpg')
my_image = PIL.Image.open(filename)

# Assign the length and width of my_image to variables for later use
width = my_image.size[0]
length = my_image.size[1]

# Create my_mask, a black rectangle with transparency in some pixels
my_mask = PIL.Image.new('RGBA', (width, length), (0, 100, 0, 0))
drawing_layer = PIL.ImageDraw.Draw(my_mask)
drawing_layer.ellipse((125, 20, 250, 150), fill=(255, 50, 0, 255))
drawing_layer.ellipse((125, 20, 250, 168), fill=(255, 50, 0, 255))
drawing_layer.ellipse((125, 20, 250, 168), fill=(255, 50, 0, 255))
drawing_layer.ellipse((125, 20, 250, 168), fill=(255, 50, 0, 255))

# Apply my_mask as a mask to my_image, creating the result
result = PIL.Image.new('RGBA', (width, length))
result.paste(my_image,(-100,0), mask=my_mask)
result.paste(my_image,(60,0), mask=my_mask)
result.paste(my_image,(-100,200), mask=my_mask)
result.paste(my_image,(60,200), mask=my_mask)

fig, axes = plt.subplots(1, 3)
for i in range(3):
    axes[i].axis('on')
axes[0].imshow(my_image, interpolation='none')
axes[0].set_title('my_image')
axes[1].imshow(my_mask, interpolation='none')
axes[1].set_title('my_mask')
axes[2].imshow(result, interpolation='none')
axes[2].set_title('result')
fig.show()