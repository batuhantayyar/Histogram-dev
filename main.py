# Batuhan Tayyar 02205076043
import cv2
import numpy as np
import matplotlib.pyplot as plt

# resmi gösterme
img = cv2.imread("robot.png")
s = img.shape
cv2.imshow('normal resim ', img)

# BGR den gri forma renkleri çevir
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gri form', img_gray)

# histogramı hesaplama
H = np.zeros(shape=(256, 1))
# matris s değerinde
for i in range(s[0]):
    for j in range(s[1]):
        k = img_gray[i, j]
        H[k, 0] = H[k, 0] + 1

# histogramı yazdirma
plt.plot(H)
plt.show()
cv2.waitKey(0)
