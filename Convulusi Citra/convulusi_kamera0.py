#G64160017
import numpy as np
import cv2

# camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
camera = cv2.VideoCapture("azumanga-azumanga-daioh.gif")#

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 600)#Mengatur lebar frame menjadi 600 piksel
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)#Mengatur tinggi frame menjadi 400 piksel

#konvolusi manual
def konvolusi(image, kernel):# Fungsi untuk melakukan konvolusi manual antara gambar dan kernel
    row,col= image.shape# Mendapatkan ukuran baris dan kolom gambar
    mrow,mcol=kernel.shape# Mendapatkan ukuran baris dan kolom kernel
    
    h = int(mrow/2)# Menghitung nilai setengah dari ukuran kernel untuk menggeser indeks

    canvas = np.zeros((row,col),np.uint8)# Membuat kanvas kosong dengan ukuran yang sama dengan gambar, bertipe uint8 (8-bit)
    for i in range(0,row):# Loop untuk mengiterasi setiap piksel pada gambar
        for j in range(0,col):
            if i==0 or i==row-1 or j==col-1:# Jika berada di tepi gambar, lewati proses konvolusi
                canvas.itemset((i,j),0)
                continue
            imgsum=0# Variabel untuk menyimpan hasil konvolusi pada setiap piksel
            for k in range (-h, mrow-h):
                for l in range (-h, mcol-h):# Menghitung hasil perkalian antara piksel dan kernel
                    res=image[i+k,j+l] * kernel[h+k,h+l]
                    imgsum+=res# Menjumlahkan hasil perkalian
                canvas.itemset((i,j), imgsum)# Menyimpan hasil konvolusi ke kanvas
    return canvas

def kernel1(image):# Fungsi yang menerapkan kernel pertama (High Pass Filter)
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32) # Kernel yang digunakan untuk edge detection (deteksi tepi) atau high-pass filter
    canvas = konvolusi(image, kernel) # Melakukan konvolusi antara gambar dan kernel
    # print("Hasil konvolusi kernel1 = ", canvas)
    return canvas

def kernel2(image):# Fungsi yang menerapkan kernel kedua (Low Pass Filter)
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)# Kernel yang digunakan untuk smoothing (pelembutan) atau low-pass filter
    canvas2 = konvolusi(image, kernel)# Melakukan konvolusi antara gambar dan kernel
    # print("Hasil konvolusi kernel2 = ", canvas2)
    return canvas2

while True:
    ret, frame = camera.read() # Membaca frame dari gif
    #frame = cv2.flip(frame, 1)
    image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#Mengubah gambar dari mode BGR (Blue, Green, Red) menjadi grayscale (hitam putih).
    test1 = kernel1(image1)#Memanggil fungsi kernel1() untuk menerapkan filter high pass filter (HPF) pada gambar image1
    print("gambar1 ordo = ", image1.shape)#Mencetak ordo (dimensi) dari gambar asli (image1)
    print("gambar1 ori = ", image1)#Mencetak isi dari matriks gambar grayscale (image1)
    print("gambar1 HPF ordo = ", test1.shape)#Mencetak dimensi (ordo) dari gambar yang telah difilter dengan high pass filter (HPF) (test1)
    print("gambar1 HPF = ", test1)#Mencetak isi dari matriks hasil konvolusi setelah diterapkan filter HPF (test1)
    #cv2.imshow("gambar1",image1)
    cv2.imshow("High pass",test1)#Menampilkan gambar yang telah difilter dengan HPF

    test2=kernel2(image1)#Memanggil fungsi kernel2() untuk menerapkan low pass filter (LPF) pada gambar image1
    print("gambar2 ori ordo = ", image1.shape)#Mencetak ordo (dimensi) gambar asli, image1
    print("gambar2 ori = ", image1)#Mencetak isi dari matriks gambar asli (image1)
    print("gambar1 LPF ordo = ", test2.shape)#Mencetak ordo (dimensi) dari gambar yang telah difilter dengan low pass filter (LPF) (test2
    print("gambar2 LPF = ", test2)#Mencetak isi dari matriks hasil konvolusi setelah diterapkan LPF (test2).
    #cv2.imshow("gambar2",image1)
    cv2.imshow("low pass",test2)#Menampilkan gambar yang telah difilter dengan LPF

    if cv2.waitKey(1) == ord('q'):#Fungsi cv2.waitKey(1) menunggu input dari keyboard selama 1 milidetik, dan jika tombol 'q' ditekan, kondisi ini akan bernilai True dan program akan keluar dari loop
        break

camera.release()
cv2.destroyAllWindows()#Menutup semua jendela yang dibuka oleh OpenCV selama program berjalan.
#Kesimpulan
'''
Program ini menerapkan operasi konvulusi manual pada gambar menggunakan 2 jenis kernel,
yaitu High Pass Filter (HPF) dan Low Pass Filter(LPF), HPF di gunakan untuk menonjolkan
tepi pada vidio, sedangkan LPF digunakan untuk menghaluskan vidio.

pada program juga di tampilkan setiap ukuran dari piksel asli, piksel HPF dan LPF, dimensi gambar asli, dimensi HPF dan LPF
untuk melihat perbedaan ukuran antara test1 dan test2
ukuran dimensi akan terus berubah karena vidio bergerak terus

spesifikasi laptop:
Device name	LAPTOP-G7E8L34K
Processor	12th Gen Intel(R) Core(TM) i5-12500H   2.50 GHz
Installed RAM	16,0 GB (15,7 GB usable)

'''
