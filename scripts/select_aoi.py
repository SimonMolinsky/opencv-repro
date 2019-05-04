import cv2
import numpy as np
import matplotlib.pyplot as plt


class SelectAreaOfInterest():
    def __init__(self, ax, img):
        self.img = img
        self.points = []
        self.lines = []
        self.figure = plt.figure(1)
        self.circle_img = np.copy(img)
        self.circle_diameter = 30
        self.is_circle = True
        self.lines_img = np.copy(img)
        self.line_thickness = 15
        self.is_line = False
        self.ax = ax
        self.color_circle = (255, 0, 255)
        self.color_line = (0, 255, 255)
        self.db_click = False

        self.status = 'circles'

        canvas = self.figure.canvas
        canvas.mpl_connect('button_press_event', self.button_press_callback)
        canvas.mpl_connect('button_release_event', self.button_release_callback)
        canvas.mpl_connect('scroll_event', self.button_scroll_callback)


    ### EVENTS ###

    def button_press_callback(self, event):
        if (event.button == 1 and event.dblclick == True):
            self.db_click = True
            self.points.append((int(event.xdata), int(event.ydata)))
            cv2.circle(self.circle_img, self.points[-1], self.circle_diameter, self.color_circle, -1)
        elif event.button == 3:
            if self.status == 'circles':
                print('Use mouse scroll button to change the ROI, then press right mouse button')
                self.is_circle = False
                self.is_line = True
                for line in self.prepare_lines():
                    cv2.line(self.lines_img, line[0], line[1], self.color_line, self.line_thickness)
                self.status = 'lines'
            elif self.status == 'lines':
                self.is_line = False
                print('Data processing... Close window to go further')

    def button_release_callback(self, event):
        if ((self.db_click == True and self.is_circle == True) or self.is_line == True):
            self.db_click = False
            self.ax.images.pop()
            if self.is_circle:
                self.ax.imshow(self.circle_img, alpha=0.2)
            elif self.is_line:
                self.ax.imshow(self.lines_img, alpha=0.4)
            plt.draw()

    def button_scroll_callback(self, event):
        if self.is_line == True:
            if event.button == 'up':
                self.line_thickness = self.line_thickness + 2
            else:
                self.line_thickness = self.line_thickness - 1
            self.clear_lines()
            for line in self.prepare_lines():
                cv2.line(self.lines_img, line[0], line[1], self.color_line, self.line_thickness)
            self.ax.images.pop()
            self.ax.imshow(self.lines_img, alpha=0.4)
            plt.draw()

    def clear_lines(self):
        self.lines_img = np.copy(self.img)
        return 0
        


    ### PROCESSING ###


    def prepare_lines(self):
        pt_len = len(self.points)
        for i in range(0, pt_len-1):
            pt1 = self.points[i]
            pt2 = self.points[i+1]
            self.lines.append([pt1, pt2])
        return self.lines


class SelectPoints():

    def __init__(self, ax, img):
        self.img = img
        self.points = []
        self.figure = plt.figure(1)
        self.circle_img = np.copy(img)
        self.circle_diameter = 5
        self.is_circle = True
        self.ax = ax
        self.color_circle = (255, 0, 0)
        self.db_click = False

        canvas = self.figure.canvas
        canvas.mpl_connect('button_press_event', self.button_press_callback)
        canvas.mpl_connect('button_release_event', self.button_release_callback)

    ### EVENTS ###

    def button_press_callback(self, event):
        if (event.button == 1 and event.dblclick == True):
            self.db_click = True
            self.points.append((int(event.xdata), int(event.ydata)))
            cv2.circle(self.circle_img, self.points[-1], self.circle_diameter, self.color_circle, -1)
        elif event.button == 3:
            print('You have stored all points, close the window to end a program')

    def button_release_callback(self, event):
        if self.db_click == True:
            self.db_click = False
            self.ax.images.pop()
            self.ax.imshow(self.circle_img, alpha=0.2)
            plt.draw()
