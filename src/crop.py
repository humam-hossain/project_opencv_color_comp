import cv2 as cv

ref = cv.imread("../photos/complex_original.jpg")
ref2 = cv.imread("../photos/comlex_sample.jpg")

ref = ref[1000:-1000, 500:-500]
ref2 = ref2[1000:-1000, 500:-500]

print(ref.shape)
print(ref2.shape)

cv.imwrite("complex_original.jpg", ref)
cv.imwrite("complex_sample.jpg", ref2)


cv.waitKey(0)