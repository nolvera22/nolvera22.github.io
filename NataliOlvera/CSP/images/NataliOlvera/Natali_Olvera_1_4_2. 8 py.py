'''
JDoe_JSmith_1_4_2:
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np

''' Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'women.jpg')
# Read the image data into an array
img = plt.imread(filename)

''' Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1,1)
#show the image data in a subplot
ax.imshow(img, interpolation= 'none')
#show the figure on the screen
height = len(img)
width = len(img[0])
for row in range(431, 459):
    for column in range(138, 160):
        img[row] [column] = [255, 0, 255]
fig.show()