# Citra-Digital
---

### **1. Convert Color**
**Konversi Warna** adalah proses mengubah ruang warna citra dari satu model ke model lainnya. Contohnya: 
- Dari RGB ke Grayscale.
- Dari RGB ke HSV (Hue, Saturation, Value).
**Tujuan**:
- Mempermudah analisis citra (misalnya analisis fitur lebih sederhana dalam Grayscale).
- Menyesuaikan format untuk algoritma tertentu.

**Contoh:**
```python
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
```
Gambar Asli:

<img width="200" height="200" src="https://github.com/user-attachments/assets/a3017bb8-8003-4def-a3be-5f2b40184d1c" alt="Bidang">

Gambar Grayscale:

<img width="200" height="200" src="https://github.com/user-attachments/assets/84a2a934-2456-4ba7-862d-7d2cf123559a" alt="Screenshot 2024-11-20 215012">

- Mengubah citra berwarna (BGR) menjadi grayscale.
---

### **2. Konvolusi Citra**
**Konvolusi Citra** adalah operasi matematika di mana kernel/filter (matriks kecil) diaplikasikan ke seluruh piksel citra untuk menghasilkan efek tertentu, seperti:
- **Blur (mengaburkan)**.
- **Sharpening (penajaman)**.
- **Edge detection (pendeteksian tepi)**.
- **High Pass Filter (HPF) dan Low Pass Filter(LPF)**.
**Contoh:**
```python
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
```

Gambar HPF dab LPF:

<img width="400" height="200" src="https://github.com/user-attachments/assets/0f23f8ac-672a-41d5-9fee-83d26937d3cba" alt="image">

---

### **3. Ekstraksi Ciri**
**Ekstraksi Ciri** adalah proses mendeteksi dan mengekstrak informasi penting dari citra, seperti:
- **BENTUK**
- **UKURAN**
- **GEOMETRI**

**Tujuan**:
- Representasi data citra dalam bentuk yang lebih informatif dan efisien untuk digunakan pada tugas-tugas seperti pengenalan pola atau klasifikasi.

**Contoh:**
```python
circularity = (4 * np.pi * area) / (perimeter * perimeter) if perimeter > 0 else 0
# Tentukan apakah bulat atau tidak bulat
label = "Bulat" if 0.8 <= circularity <= 1.2 else "Tidak Bulat"
```
Gambar menentukan bentuk lingkaran dan bukan lingkaran:

<img width="200" height="200" src="https://github.com/user-attachments/assets/b935ce1f-f09f-41e3-98e9-e00f67b8fd05" alt="image">

---
### **4. Evaluate Image Quality**
**Evaluasi Kualitas Citra** adalah untuk mengevaluasi kualitas atau perbedaan antara dua gambar (misalnya, gambar asli dan gambar hasil rekonstruksi atau kompresi), seperti:
- **MSE dan PSNR**
- **Mean, Standard Deviasi, dan Kovarian**
- **Structural Similarity (SSIM)**
- **Normalized Correlation (NC)**
- **Bit Error Rate (BER)**
  
**Contoh:**
```python
def PSNR(original, compressed): 
	mse = np.mean((original - compressed) ** 2) 
	if(mse == 0): # MSE is zero means no noise is present in the signal . 
				# Therefore PSNR have no importance. 
		return 100
	max_pixel = 255.0
	psnr = 20 * log10(max_pixel / sqrt(mse)) 
	return psnr 
```

Nilai yang di dapat dari dua gambar yang sudah di original dan Kompres
Gambar Asli:

<img width="200" height="200" src="https://github.com/user-attachments/assets/9cd8d9f7-843c-406b-8c42-2c768e67bd0d" alt="bidang">

Gambar Kompres:

<img width="200" height="200" src="https://github.com/user-attachments/assets/95eb2bed-5ee5-4029-890a-0afbb0123a05" alt="c_bidang">

PSNR value is 39.65158686265894 dB

---

### **5. Morfologi Citra**
**Morfologi Citra** adalah operasi berbasis bentuk (shape-based) yang digunakan pada citra biner atau grayscale, termasuk:
- **Erosi**: Mengurangi ukuran objek.
- **Dilasi**: Memperbesar objek.
- **Opening**: Menghilangkan noise kecil.
- **Closing**: Menutup celah dalam objek.

**Contoh:**
```python
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
```
Gambar erosi:

<img width="400" height="200" src="https://github.com/user-attachments/assets/e964a75f-f722-4b43-aef1-c3f560c96532" alt="image">

---

### **6. Restorasi Citra**
**Restorasi Citra** adalah proses memperbaiki citra yang rusak akibat:
- **Noise**.
- **Blur**.
- **Artefak kompresi**.

**Metode**:
- **Median Filter**
- **Gaussian Filter**
- **Averanging Filter**
- **Bilateral Filter**
- **Low Pass Filter dan High Pass Filter**

**Contoh:**
```python
low_pass = cv2.blur(img, (5, 5))
kernel = np.array([[-1, -1, -1],
                  [-1, 8, -1],
                  [-1, -1, -1]])
high_pass = cv2.filter2D(img, -1, kernel)
```
Gambar LPF dan HPF:

<img width="400" height="200" src="https://github.com/user-attachments/assets/10297033-41dd-4906-b49c-49f1faf1dfd0" alt="image">

---

### **7. Segmentasi Citra**
**Segmentasi Citra** adalah proses membagi citra menjadi beberapa wilayah (regions) berdasarkan karakteristik tertentu, seperti warna, intensitas, atau tekstur.

**Tujuan**:
- Memisahkan objek dari latar belakang.
- Analisis lebih mudah pada bagian tertentu dari citra.

**Metode**:
- **Thresholding**: Membagi berdasarkan intensitas.
- **Edge Detection**: Mendeteksi batas objek.
- **Clustering**: Metode seperti K-Means.

**Contoh:**
```python
canny = cv2.Canny(img, 100, 200)
```
Gambar Asli:

<img width="200" height="200" src="https://github.com/user-attachments/assets/17fb0e22-ceaa-4517-95e0-60a7da6d09a3" alt="image">

Gambar deteksi tepi canny:

<img width="200" height="200" src="https://github.com/user-attachments/assets/70c815b5-85c0-40ec-b424-c3c241773d65" alt="image">

---

### **8. Transformasi Citra**
**Transformasi Citra** adalah operasi untuk memodifikasi posisi, orientasi, atau representasi citra. Contohnya:
- **Rotasi**: Memutar citra.
- **Scaling**: Mengubah ukuran citra.
- **Translasi**: Menggeser Citra.
- **Skala**: Mengubah ukuran citra dengan memperbesar atau memperkecil.
- **Affine**: Kombinasi transformasi linier (rotasi, scaling, translasi, atau shearing) yang mempertahankan garis lurus dan paralelisme.

**Contoh:**
```python
MTranslasi = np.float32([
     [2, 0, 100],
     [0, 2, 50]           
    ])
print(MTranslasi, '\n')
dst = cv2.warpAffine(img, MTranslasi, (coloms, baris))
```
Gambar Asli:

<img width="200" height="200" src="https://github.com/user-attachments/assets/af774ee6-06ed-4af1-9cb1-b3a4797adf6c" alt="image">

Gambar Translasi:

<img width="200" height="200" src="https://github.com/user-attachments/assets/3b7d24eb-8c22-406a-992c-f07cc9b21a00" alt="image">
