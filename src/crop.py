import cv2 as cv

def rescaleImg(img, scale=0.75):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)

    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

ref = cv.imread("../photos/ref.jpg")
ref2 = cv.imread("../photos/ref2.jpg")


ref = ref[1000:-1000, 500:-500]
ref2 = ref2[1000:-1000, 500:-500]

print(ref.shape)
print(ref2.shape)

cv.imwrite("ref1.jpg", ref)
cv.imwrite("ref2.jpg", ref2)

scale = 0.2
cv.imshow("ref", rescaleImg(ref, scale))
cv.imshow("ref2", rescaleImg(ref2, scale))


cv.waitKey(0)