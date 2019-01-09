# fix some crash problem on mac os x.
import sys
if sys.platform == 'darwin':
    import matplotlib
    matplotlib.use('TkAgg')

from matplotlib import pyplot as plt
from matplotlib import patches as patches
from PIL import Image
import numpy as np


"""
Most plt tutorials use simplified API, which is easy to write but hard to understand and remember.
Instead the OOP API is easy to understand and remember, and you just need to write a little more code.

Core Object:
1. Figure: the whole picture
2. Axes: sub area in the picture, create by add_subplot on figure object.

Core Logic:
1. Create Figure object.
2. Create each Axes object.
3. Draw something on each Axes object, set title, ticks and something else.
4. Finally, call plt.show() to display the result.
"""


def plt_demo():
    # read image, shape: (height, width, channel). Channel order is rgb. When use opencv, default channel order is bgr.
    image_path = 'test.jpg'
    img = Image.open(image_path)
    img_array = np.array(img)
    h, w, c = img_array.shape

    # create figure obj
    fig = plt.figure()

    axes1 = fig.add_subplot(1, 2, 1)
    axes1.imshow(img)   # you can use PIL.Image object, or just numpy array.
    axes1.set_title('First')
    axes1.set_xticks([])
    axes1.set_yticks([])

    # create axes obj
    axes2 = fig.add_subplot(1, 2, 2)
    axes2.imshow(img_array)
    axes2.set_title('Second')
    axes2.set_xticks([0, w/2, w])
    axes2.set_yticks([0, h/2, h])

    # draw rect region
    left = 150
    top = 190
    width = 600
    height = 310
    rect = patches.Rectangle((left, top), width, height, linewidth=1, edgecolor=(1, 0, 0, 1), facecolor='None')
    axes2.add_patch(rect)

    # draw attention value text
    text_pad = 1
    axes2.text(left + text_pad + 1, top - text_pad - 2, 'Tank', color='b', fontsize=8,
               bbox=dict(pad=1, edgecolor='None', facecolor='white', alpha=0.8))

    # show result
    plt.show()


if __name__ == '__main__':
    plt_demo()
