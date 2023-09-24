# here we plan to develop cool tools for ml

import matplotlib.pyplot as plt
from skimage import io


def show_image(path):
    img = io.imread(path)
    plt.figure()
    plt.imshow(img)
    plt.axis("off")
    plt.show()
