import cv2
import numpy as np
import matplotlib.pyplot as plt


class SelectAreaOfInterest():
    def __init__(self, ax, img):
        self.points = []
        self.figure = plt.figure(1)
        self.img = img
        self.circle_diameter = 30
        self.ax = ax
        self.color = (255, 0, 255)

        canvas = self.figure.canvas
        canvas.mpl_connect('button_press_event', self.button_press_callback)
        canvas.mpl_connect('button_release_event', self.button_release_callback)

    def button_press_callback(self, event):
        self.points.append((int(event.xdata), int(event.ydata)))
        cv2.circle(self.img, self.points[-1], self.circle_diameter, self.color, -1)

    def button_release_callback(self,click):
        self.ax.images.pop()
        self.ax.imshow(self.img, alpha=0.2)
        plt.draw()


def draw_mask(base_image):
    img = cv2.imread(base_image)
    upper_layer = np.zeros(img.shape, np.uint8)
    ax = plt.subplot(111)
    ax.imshow(img)
    ax.imshow(upper_layer, alpha=0.02)
    
    paint = SelectAreaOfInterest(ax, upper_layer)
    plt.show()

image = 'check.png'
draw_mask(image)
