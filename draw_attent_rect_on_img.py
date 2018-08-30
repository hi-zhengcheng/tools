import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches


# read image
# matplotlib.image only support png by default.
# install PIL to make matplotlib.image can handle jpg and other formats.
IMG_PATH = 'path to jpg file'
img = mpimg.imread(IMG_PATH)

# create figure obj
fig = plt.figure()

# create axes obj
axes = fig.add_subplot(1, 1, 1)
axes.imshow(img)

# draw attention rect region
left = 10
top = 10
width = 200
height = 150
rect = patches.Rectangle((left, top), width, height, linewidth=1, edgecolor=(1, 0, 0, 1), facecolor='None')
axes.add_patch(rect)

# draw attention value text
text_pad = 1
axes.text(left + text_pad + 1, top - text_pad - 2, '0.8523', color='b', fontsize=8, bbox=dict(pad=1, edgecolor='None', facecolor='white', alpha=0.8))

# show text
plt.show()

