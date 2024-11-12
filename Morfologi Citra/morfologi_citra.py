# Mengimpor pustaka OpenCV, NumPy, dan pyplot dari matplotlib
import cv2
import numpy as np
from matplotlib import pyplot as plt 

# Membaca citra 'oye.jpg' dalam format grayscale
img = cv2.imread('oye.jpg',0)
# Membaca citra 'yeye.jpg' dalam format grayscale
img0 = cv2.imread('yeye.jpg',0)
# Membaca citra 'demon.jpg' dalam format grayscale
imgC = cv2.imread('demon.jpg',0)

# (Dikomentari) Mengubah ukuran citra menjadi 500x500 piksel (jika diperlukan)
# img = cv2.resize(img,(500,500))
# img0 = cv2.resize(img0,(500,500))
# imgC = cv2.resize(imgC,(500,500))

# Membuat kernel berbentuk matriks 5x5 dengan nilai 1 (digunakan untuk operasi morfologi)
kernel = np.ones((5,5), np.uint8)
# Melakukan operasi erosi pada citra 'img' menggunakan kernel yang telah dibuat
erosion = cv2.erode(img, kernel, iterations=1)
# Melakukan operasi dilasi pada citra 'img' menggunakan kernel yang telah dibuat
dilation = cv2.dilate(img, kernel, iterations=1)
# Melakukan operasi opening pada citra 'img0' menggunakan kernel
opening = cv2.morphologyEx(img0, cv2.MORPH_OPEN, kernel)
# Melakukan operasi closing pada citra 'imgC' menggunakan kernel
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE, kernel)
# Daftar judul untuk setiap citra yang akan ditampilkan
titles = ['Normal Image', 'Erosion', 'Dilation', 'Before Opening', 'Opening', 'Before Closing', 'Closing']
# Daftar citra yang akan ditampilkan
images = [img, erosion, dilation, img0, opening, imgC, closing]
# Loop untuk menampilkan setiap citra dan judulnya
for i in range(7):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], 'gray')  # Menampilkan citra dalam skala abu-abu
    plt.title(titles[i])            # Menampilkan judul citra
    plt.xticks([])                  # Menghilangkan sumbu x
    plt.yticks([])                  # Menghilangkan sumbu y
# Menampilkan semua hasil pengolahan citra dalam satu jendela
plt.show()
# (Dikomentari) Menampilkan citra 'closing' dan 'imgC' di jendela baru (jika diperlukan)
# cv2.imshow("img", closing)
# cv2.imshow("imgC", imgC)
# cv2.waitKey(0)  # Menunggu tombol ditekan sebelum menutup jendela
# cv2.destroyAllWindows()