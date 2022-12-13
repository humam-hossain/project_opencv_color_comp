from skimage.metrics import structural_similarity
import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    # images, videos and live videos

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

original = cv.imread("../photos/original.jpg")
sample = cv.imread("../photos/sample.jpg")

original = cv.resize(original, (500, 500), interpolation=cv.INTER_LINEAR)
sample = cv.resize(sample, (500, 500), interpolation=cv.INTER_LINEAR)

# grayscaling images for color intensity
original_gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
sample_gray = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

# computing differences
(score, diff) = structural_similarity(original_gray, sample_gray, full=True)
print("Image Similarity: {:.4f}%".format(score * 100))

diff = (diff * 255).astype("uint8")
diff_box = cv.merge([diff, diff, diff])


# threshing
ret, thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

print(len(contours))

mask = np.zeros(original.shape, dtype="uint8")
filled_sample = sample.copy()

for c in contours:
    area = cv.contourArea(c)
    
    if area > 100:
        cv.drawContours(mask, [c], 0, (255,255,255), -1)
        cv.drawContours(filled_sample, [c], 0, (0,255,0), -1)

cv.imshow("original rgb", original)
cv.imshow("Sample Color", sample)
cv.imshow("Diff", diff)
# cv.imshow("Diff Box", diff_box)
# cv.imshow("Thresh", thresh)
# cv.imshow("Mask", mask)
# cv.imshow("Filled Sample", filled_sample)

cv.waitKey(0)