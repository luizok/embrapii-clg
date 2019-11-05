import numpy as np
from matplotlib import pyplot as plt
import cv2
from sklearn.cluster import KMeans
from pprint import pprint


PATH = './cartas'
plt.style.use('seaborn-dark')

def plot_colors(hist, centroids):

    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    print('\tMost Frequent Colors')
    for (percent, color) in zip(hist, centroids):
        print('\t\t{} -> {}'.format(color, percent))
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
            color.astype("uint8").tolist(), -1)
        startX = endX

    return bar


def centroid_histogram(clt):

    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    hist, _ = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist


def clusterize(img):

    img = img.reshape((img.shape[0] * img.shape[1], 3))
    clt = KMeans(n_clusters=7)
    clt.fit(img)

    return clt


def get_bar_color(idx, img, save=True):

    clt = clusterize(img)

    hist = centroid_histogram(clt)
    bar = plot_colors(hist, clt.cluster_centers_)

    if save:
        plt.imshow(bar)
        plt.savefig('./{}/{}/bar_color.png'.format(PATH, idx), bbox_inches='tight', pad_inches=0)

    return bar


def blur_threshold(idx, img, save=True):

    blur = cv2.GaussianBlur(img, (7, 7), 0)
    thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)[1]

    if save:
        plt.imshow(thresh)
        plt.savefig('./{}/{}/blur_threshold.png'.format(PATH, idx), bbox_inches='tight', pad_inches=0)

    return thresh


def get_edges(idx, img, save=True):

    img = blur_threshold(idx, img, False)
    conts = cv2.Canny(img, 100, 200)

    if save:
        plt.imshow(conts)
        plt.savefig('./{}/{}/canny_edge.png'.format(PATH, idx), bbox_inches='tight', pad_inches=0)

    return conts


def extract_infos(idx):

    filename = './{}/{}/carta.jpeg'.format(PATH, idx)
    print(filename)

    img = cv2.imread(filename)
    print('\tsize -> {}'.format(img.shape[:2]))

    get_bar_color(idx, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    blur_threshold(idx, cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    get_edges(idx, cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))


plt.axis('off')
plt.tick_params(
    axis='both',
    left='off',
    top='off',
    right='off',
    bottom='off',
    labelleft='off',
    labeltop='off',
    labelright='off',
    labelbottom='off'
)

for i in range(5):
    extract_infos(i+1)

    
