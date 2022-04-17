import matplotlib.pyplot as plt
import cv2

def display_image_in_actual_size(im_data):
    """
    plots as per the image size.
    :param im_data: image cv2 object/ numpy ndarray
    :return: nothing
    """
    dpi = 80
    # im_data = plt.imread(im_path)
    height, width, depth = im_data.shape
    figsize = width / float(dpi), height / float(dpi) # plot size in inches
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off') # Hide spines, ticks, etc.
    ax.imshow(im_data, cmap='gray')
    plt.show()