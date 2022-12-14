import cv2 as cv
import numpy as np

def process(original, sample, bias=1000):
    # grayscaling samples
    original_gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
    sample_gray = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

    # computing differences
    diff = 255 - cv.absdiff(sample_gray, original_gray)

    # thresh & contour
    ret, thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    contours, hiererchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    mask = np.zeros(original.shape, dtype="uint8")
    filled_sample = sample.copy()

    # visualising the differences in mask & sample
    for c in contours:
        area = cv.contourArea(c)
        if area > bias:
            cv.drawContours(mask, [c], 0, (255,255,255), -1)
            cv.drawContours(filled_sample, [c], 0, (0,255,0), -1)

    # result

    images = [
        ["original", original],
        ["sample", sample],
        ["diff", diff],
        ["thresh (THRESH_BINARY_INV)", thresh],
        [f'Output, contour area > {bias}', filled_sample],
        [f'mask, contour area > {bias}', mask]
    ]

    return (contours, images)