import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar dari file 'demon.jpg'
img = cv2.imread('demon.jpg')

# Menerapkan Low-pass filter dengan kernel rata-rata
low_pass = cv2.blur(img, (5, 5))

# Menerapkan High-pass filter dengan kernel khusus
# Kernel High-pass untuk menonjolkan tepi
kernel = np.array([[-1, -1, -1], 
                   [-1, 8, -1], 
                   [-1, -1, -1]])
high_pass = cv2.filter2D(img, -1, kernel)

# Judul untuk setiap gambar yang difilter
titles = ['Gambar Asli', 'Low-pass Filter', 'High-pass Filter']
# Mengumpulkan semua gambar (hasil filter) ke dalam sebuah list
images = [img, low_pass, high_pass]

# Mengatur ukuran plot (12x8 inci)
plt.figure(figsize=(12, 8))

# Loop untuk menampilkan setiap gambar dan histogramnya
for i in range(3):
    # Menampilkan gambar di subplot kiri (kolom ganjil)
    plt.subplot(3, 2, 2*i+1)
    # Mengubah gambar dari BGR ke RGB agar warna tampil dengan benar di matplotlib
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    # Menetapkan judul untuk gambar
    plt.title(titles[i])
    # Menghilangkan sumbu x dan y pada tampilan gambar
    plt.xticks([]), plt.yticks([])

    # Menampilkan histogram pada subplot kanan (kolom genap)
    color = ('b', 'g', 'r')  # Daftar warna untuk histogram (biru, hijau, merah)
    plt.subplot(3, 2, 2*i+2)
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
# Menampilkan semua gambar dan histogramnya
plt.show()
