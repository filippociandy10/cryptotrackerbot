import cv2
from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt


def detectimage(image, template, threshold=0.75):
    im2copy = image.copy()
    # template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    h, w = template.shape[0], template.shape[1]

    im = im2copy.copy()
    # im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(im, template, cv2.TM_CCOEFF_NORMED)

    loc = np.where(res >= threshold)
    array = []

    for pt in zip(*loc[::-1]):
        # p_buy = res[pt[1], pt[0]]
        array.append((pt[0], pt[1]))
        cv2.rectangle(im2copy, pt, (pt[0] + w, pt[1] + h),
                      (0, 0, 255 * (res[pt[1], pt[0]] - 0.8)*5), 2)
    return array


def plot(image, target_plot, template, color):
    buy_coordinates = detectimage(image, template)
    for pt in buy_coordinates:
        cv2.rectangle(target_plot, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]),
                      color, 2)


def plotlist(coordinate_list):
    fig, ax = plt.subplots()
    x = [pt[0] for pt in coordinate_list]
    y = [pt[1] for pt in coordinate_list]
    ax.scatter(x, y)
    plt.show()


def filterduplicates(coordinates):
    cluster = AgglomerativeClustering(n_clusters=None, distance_threshold=15)
    cluster_dict = {}
    cluster_ids = (cluster.fit_predict(coordinates))
    for idx, cluster_id in enumerate(cluster_ids):
        cluster_dict[cluster_id] = coordinates[idx]
    return list(cluster_dict.values())


def determine(image):
    buy_image = cv2.imread("Template/buy.png")
    sell_image = cv2.imread("Template/sell.png")
    buy_coordinates = filterduplicates(detectimage(
        cv2.imread("pictures/screenshot.png"), buy_image))
    sell_coordinates = filterduplicates(detectimage(
        cv2.imread("pictures/screenshot.png"), sell_image))
    (sell_coordinates.sort(key=lambda tup: tup[0]))
    buy_coordinates.sort(key=lambda tup: tup[0])
    x_buy = buy_coordinates[-1][0]
    x_sell = sell_coordinates[-1][0]
    x_max = max(x_buy, x_sell)
    # cv2.imshow("Image", image)
    cv2.waitKey(0)
    if (x_buy > x_sell):
        # print("BUY!")
        return "BUY", x_max
    else:
        # print("SELL!")
        return "SELL", x_max
