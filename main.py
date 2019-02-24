import cv2
import numpy as np
import matplotlib.pyplot as plt

from select_aoi import SelectAreaOfInterest


def draw_mask(base_image):
    img = cv2.imread(base_image)
    upper_layer = np.zeros(img.shape, np.uint8)
    ax = plt.subplot(111)
    ax.imshow(img)
    ax.imshow(upper_layer, alpha=0.02)
    
    paint = SelectAreaOfInterest(ax, upper_layer)
    plt.show()


if __name__ == '__main__':
    image = 'check.png'
    draw_mask(image)
