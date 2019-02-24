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


def segment_region(image, thresh_lower, filter_image=True):
    if filter_image:
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


def reproject_masked_region(masked_region, coordinates, thickness):
    pass


def test_point(x, pair_of_coordinates, last=False):
    p1 = pair_of_coordinates[0]
    p2 = pair_of_coordinates[1]
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]
    slope = (y2 - y1) / (x2 - x1)

    if (x >= 0 and x < x1) or (x > x1 and x < x2):
        y = slope * (x - x1) + y1
        return np.floor(y)
    elif (x > x2 and last):
        y = slope * (x - x2) + y2
        return np.floor(y)
    elif x == x1:
        return y1
    elif x == x2:
        return y2
    else:
        return 0
    


def project_to_horizontal_line(masked_region, coordinates, thickness):
    t = 2 * int(thickness / 2)
    image_slice = np.zeros((t, masked_region.shape[1], 3))
    coordinates_list = []
    xs = range(0, masked_region.shape[1])

    for i in xs:
        for c in coordinates:

            if c == coordinates[-1]:
                yt = test_point(i, c, True)
            else:
                yt = test_point(i, c, False)

            if yt == 0:
                pass
            else:
                coordinates_list.append([i, yt])
                break

    for i in xs:
        dy_bottom = int(coordinates_list[i][1] - int(thickness / 2))
        dy_top = int(coordinates_list[i][1] + int(thickness / 2))
        image_slice[:, i] = masked_region[dy_bottom:dy_top, i]

    return image_slice


if __name__ == '__main__':
    image = 'check.png'
    image = cv2.imread(image)
    roi = draw_mask(image)
    mask = mask_region(image, roi[0], roi[1])
    img_slice = project_to_horizontal_line(mask[0], roi[0], roi[1])
    plt.figure()
    plt.imshow(img_slice)
    plt.show()
    
