import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def process(original, sample, bias=1000):
    # grayscaling samples
    original_gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
    sample_gray = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

    # computing differences

    diff = 255 - cv.absdiff(sample_gray, original_gray)

    # thresh & contour
    ret, thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    contours, hiererchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print("# of contours {contours}".format(contours = len(contours)))

    mask = np.zeros(original.shape, dtype="uint8")
    filled_sample = sample.copy()

    for c in contours:
        area = cv.contourArea(c)
        if area > bias:
            cv.drawContours(mask, [c], 0, (255,255,255), -1)
            cv.drawContours(filled_sample, [c], 0, (0,255,0), -1)


    results = [
        ["original", original],
        ["sample", sample],
        ["diff", diff],
        ["thresh (THRESH_BINARY_INV)", thresh],
        [f'Output, contour area > {bias}', filled_sample],
        [f'mask, contour area > {bias}', mask]
    ]

    for img in results:
        print(img[1].shape)
        img[1] = cv.cvtColor(img[1], cv.COLOR_BGR2RGB)

    rows = 2
    cols = 3
    fig, axs = plt.subplots(rows, cols, figsize=(10, 10))
    count = 0

    fig.suptitle(f'# of contours = {len(contours)}')

    for row in range(rows):
        for col in range(cols):
            ax = axs[row][col]
            title, img = results[count]

            ax.set_axis_off()
            ax.set_title(title)
            ax.imshow(img)

            count = count + 1
    plt.tight_layout()
    plt.savefig("output_sample")
    plt.show()

original = cv.imread("../photos/tshirt_original.jpg")
sample = cv.imread("../photos/tshirt_sample_2.jpg")

bias = 1000

process(original, sample, bias)