from process import *

import cv2 as cv
import matplotlib.pyplot as plt
from tkinter import *
from PIL import ImageTk, Image 

def image_process(original, sample, bias):
    # img processing
    (contours, images) = process(original, sample, bias)
    print("# of contours {contours}".format(contours = len(contours)))

    # matplotlib figure
    for img in images:
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
            title, img = images[count]

            ax.set_axis_off()
            ax.set_title(title)
            ax.imshow(img)

            count = count + 1
    plt.show()
    plt.savefig(f'../outputs/sample_1')
    # plt.close(fig)

def gui():
    # root window
    root = Tk()
    root.title("Color Comparison by Pixel Similarity")
    root.geometry("1080x720")

    # components
    saved_outputs = ImageTk.PhotoImage(Image.open("../outputs/sample.png"))
    outputs_label = Label(image=saved_outputs)
    outputs_label.pack(side=LEFT)

    # inputs
    original = cv.imread("../photos/tshirt_original.jpg")
    sample = cv.imread("../photos/tshirt_sample_2.jpg")

    bias = 1000

    # show gui
    root.mainloop()