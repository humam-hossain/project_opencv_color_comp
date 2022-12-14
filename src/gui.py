from process import *

import cv2 as cv
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def gui():
    # root window
    root = Tk()
    root.title("Color Comparison by Pixel Similarity")
    root.geometry("1080x610")

    # img processing
    original = cv.imread("../photos/tshirt_original.jpg")
    sample = cv.imread("../photos/tshirt_sample_2.jpg")

    bias = 1000

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
    plt.savefig(f'../outputs/sample')
    plt.close(fig)
    
    # canvas = FigureCanvasTkAgg(fig, root)
    # canvas.get_tk_widget().pack(side=LEFT, fill=BOTH)

    # show gui
    root.mainloop()