from gui import *

if __name__ == "__main__":
    original = cv.imread("../photos/tshirt_original.jpg")
    sample = cv.imread("../photos/tshirt_sample_2.jpg")

    bias = 1000
    image_process(original, sample, bias)
    
    # gui()