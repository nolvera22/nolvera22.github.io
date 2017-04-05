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
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

''' Show the image data'''
# Create figure with 1 subplot
#fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
#Show the image data in the frist subplot
ax[0] .imshow(img, interpolation= 'none')
ax[1] .imshow(img)
ax[0] .set_xlim(36, 44)
ax[0] .set_ylim(80, 70)
ax[1] .set_xlim(36, 44)
ax[1] .set_ylim(80, 70)
# Show the figure on the screen
fig.show()