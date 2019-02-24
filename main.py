import cv2
import numpy as np
import matplotlib.pyplot as plt

from select_aoi import SelectAreaOfInterest


def draw_mask(base_image):
    img = base_image
    upper_layer = np.zeros(img.shape, np.uint8)
    ax = plt.subplot(111)
    ax.imshow(img)
    ax.imshow(upper_layer, alpha=0.02)
    
    paint = SelectAreaOfInterest(ax, upper_layer)
    plt.show()
    return(paint.lines, paint.line_thickness)


def mask_region(base_image, set_of_points, mask_thickness):
    print('Data processing...')
    mask = np.zeros(base_image.shape, dtype=base_image.dtype)
    for line in set_of_points:
        cv2.line(mask, line[0], line[1], (1, 1, 1), mask_thickness)
    masked_image = base_image * mask
    mean = np.mean(masked_image[masked_image > 0])
    median = np.median(masked_image[masked_image > 0])
    print('Mean: {}, median: {}'.format(mean, median))
    plt.figure()
    plt.imshow(masked_image)
    plt.show()
    return masked_image, mean, median


def segment_region(image, thresh_lower, filter_image=True):
    if filter_image:
        image = cv2.medianBlur(image, 3)
    ret, thresh = cv2.threshold(image, thresh_lower, 255, cv2.THRESH_BINARY)
    return thresh


if __name__ == '__main__':
    image = 'check.png'
    image = cv2.imread(image)
    roi = draw_mask(image)
    mask = mask_region(image, roi[0], roi[1])
    threshed = segment_region(mask[0], mask[2])
    plt.figure()
    plt.imshow(threshed)
    plt.show()
    
