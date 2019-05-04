import cv2
import numpy as np
import matplotlib.pyplot as plt


def segment_region(image, thresh_lower, filter_image=True):
    if filter_image:
        image = cv2.fastNlMeansDenoising(image, None, 10, 7, 21)
        image = cv2.medianBlur(image, 3)
    ret, thresh = cv2.threshold(image, thresh_lower, 255, cv2.THRESH_BINARY)
    return thresh


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
    plt.title('Before threshold')
    threshed = segment_region(masked_image, median)
    threshed[threshed > 0] = 1
    masked_image = masked_image * threshed
    plt.figure()
    plt.imshow(masked_image)
    plt.title('After threshold')
    plt.show()
    return masked_image, mean, median
