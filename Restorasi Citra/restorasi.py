import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('demon.jpg')
# Filter Rata-rata (Averaging), ukuran kernel 4x4
blur1 = cv2.blur(img, (4, 4))
# Filter Gaussian Blur, ukuran kernel 3x3, standar deviasi 0
blur2 = cv2.GaussianBlur(img, (3, 3), 0)
# Filter Median Blur, ukuran kernel 3 (menangani noise tipe salt-and-pepper)
median = cv2.medianBlur(img, 3)
# Filter Bilateral, diameter 9, nilai sigmaColor=75 dan sigmaSpace=75
blur3 = cv2.bilateralFilter(img, 9, 75, 75)
titles = ['Gambar Asli', 'Averaging', 'Gaussian Blur', 'Bilateral Blur',
'Median Blur']
images = [img, blur1, blur2, blur3, median]
# Mengatur ukuran plot (12x8 inci)
plt.figure(figsize=(12, 8))
# Loop untuk menampilkan setiap gambar dan histogramnya
for i in range(5):
# Menampilkan gambar di subplot kiri (kolom ganjil)
    plt.subplot(5, 2, 2*i+1)
# Mengubah gambar dari BGR ke RGB agar warna tampil dengan benar di
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
# Menetapkan judul untuk gambar
    plt.title(titles[i])
# Menghilangkan sumbu x dan y pada tampilan gambar
    plt.xticks([]), plt.yticks([])
# Menampilkan histogram pada subplot kanan (kolom genap)
    color = ('b', 'g', 'r') # Daftar warna untuk histogram (biru, hijau,
    plt.subplot(5, 2, 2*i+2)
    for j, col in enumerate(color):
# Menghitung histogram untuk setiap saluran warna (B, G, R)
        hist = cv2.calcHist([images[i]], [j], None, [256], [0, 256])
# Menampilkan plot histogram sesuai warna saluran
        plt.plot(hist, color=col)
# Mengatur batas x-axis dari 0 hingga 256
        plt.xlim([0, 256])
# Menetapkan judul untuk histogram
    plt.title(f'Histogram {titles[i]}')
# Mengatur tata letak agar tidak saling tumpang tindih
plt.tight_layout()
plt.show()