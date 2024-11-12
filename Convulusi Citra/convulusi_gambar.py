#G64160017
import numpy as np
import cv2

image1 = cv2.imread("yeye.jpg",0)# Membaca gambar pertama 'yeye.jpg'
image2= cv2.imread("yeye.jpg",0)# Membaca gambar kedua 'oye.jpg'

#konvolusi manual
def konvolusi(image, kernel):
    row,col= image.shape# Mendapatkan jumlah baris dan kolom gamba
    mrow,mcol=kernel.shape # Mendapatkan jumlah baris dan kolom kernel
    h = int(mrow/2)# Menghitung setengah ukuran kernel untuk perhitungan konvolusi (penggeseran indeks)

    canvas = np.zeros((row,col),np.uint8) # Membuat kanvas kosong dengan ukuran yang sama dengan gambar untuk menyimpan hasil konvolusi
    for i in range(0,row):
        for j in range(0,col):
            # Jika piksel berada di tepi gambar, isi dengan nilai 0
            if i==0 or i==row-1 or j==col-1:
                canvas.itemset((i,j),0)
            else:
                # Inisialisasi penjumlahan hasil konvolusi
                imgsum=0
                 # Iterasi melalui setiap nilai dalam kernel
                for k in range (-h, mrow-h):
                    for l in range (-h, mcol-h):
                        res=image[i+k,j+l] * kernel[h+k,h+l]# Menghitung hasil perkalian antara piksel gambar dan nilai kernel
                        imgsum+=res# Menambahkan hasil perkalian ke penjumlahan
                    canvas.itemset((i,j), imgsum) # Menyimpan hasil konvolusi di kanvas
    return canvas

def kernel1(image):# Fungsi untuk menerapkan filter High-Pass (HPF) menggunakan kernel tertentu
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)# Membuat kernel HPF untuk menonjolkan tepi (edge) pada gambar
    canvas = konvolusi(image, kernel) # Menerapkan konvolusi pada gambar dengan kernel HPF
    print("Hasil konvolusi kernel1 = ", canvas)# Menampilkan hasil konvolusi di konsol
    return canvas

def kernel2(image):# Fungsi untuk menerapkan filter Low-Pass (LPF) menggunakan kernel tertentu
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32) # Membuat kernel LPF untuk menghaluskan gambar dan mengurangi noise
    canvas2 = konvolusi(image, kernel)# Menerapkan konvolusi pada gambar dengan kernel LPF
    print("Hasil konvolusi kernel2 = ", canvas2)# Menampilkan hasil konvolusi di konsol
    return canvas2

test1=kernel1(image1)# Menerapkan kernel HPF pada gambar pertama dan menyimpan hasilnya di 'test1'
print("gambar1 ordo = ", image1.shape)# Menampilkan ordo (dimensi) dari gambar pertama
print("gambar1 ori = ", image1)# Menampilkan nilai piksel asli dari gambar pertama
print("gambar1 HPF ordo = ", test1.shape)# Menampilkan ordo (dimensi) dari gambar hasil filter HPF
print("gambar1 HPF = ", test1)# Menampilkan nilai piksel hasil filter HPF
#cv2.imshow("gambar1",image1)
cv2.imshow("High pass",test1)# Menampilkan gambar hasil filter HPF di jendela baru dengan nama "High pass"

test2=kernel2(image2)# Menerapkan kernel LPF pada gambar kedua dan menyimpan hasilnya di 'test2'
print("gambar2 ori ordo = ", image2.shape)# Menampilkan ordo (dimensi) dari gambar kedua
print("gambar2 ori = ", image2)# Menampilkan nilai piksel asli dari gambar kedua
print("gambar1 LPF ordo = ", test2.shape)# Menampilkan ordo (dimensi) dari gambar hasil filter LPF
print("gambar2 LPF = ", test2)# Menampilkan nilai piksel hasil filter LPF
#cv2.imshow("gambar2",image2)
cv2.imshow("low pass",test2)# Menampilkan gambar hasil filter LPF di jendela baru dengan nama "low pass"

cv2.waitKey(0)
cv2.destroyAllWindows()#Menutup semua jendela yang dibuka oleh OpenCV selama program berjalan.

#Kesimpulan
'''
Program ini menerapkan operasi konvulusi manual pada gambar menggunakan 2 jenis kernel,
yaitu High Pass Filter (HPF) dan Low Pass Filter(LPF), HPF di gunakan untuk menonjolkan
tepi pada gambar, sedangkan LPF digunakan untuk menghaluskan gambar.

pada program juga di tampilkan setiap ukuran dari piksel asli, piksel HPF dan LPF, dimensi gambar asli, dimensi HPF dan LPF
untuk melihat perbedaan ukuran antara test1 dan test2

spesifikasi laptop:
Device name	LAPTOP-G7E8L34K
Processor	12th Gen Intel(R) Core(TM) i5-12500H   2.50 GHz
Installed RAM	16,0 GB (15,7 GB usable)
'''