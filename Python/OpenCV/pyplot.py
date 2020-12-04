import cv2
from matplotlib import pyplot

img = cv2.imread('cv/woman01.jpg', cv2.IMREAD_COLOR)

b, g, r = cv2.split((img))
plot_img = cv2.merge([r, g, b])
pyplot.imshow(plot_img)
pyplot.show()
