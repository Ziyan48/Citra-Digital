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
- Mengubah citra berwarna (BGR) menjadi grayscale.
---

### **2. Konvolusi Citra**
**Konvolusi Citra** adalah operasi matematika di mana kernel/filter (matriks kecil) diaplikasikan ke seluruh piksel citra untuk menghasilkan efek tertentu, seperti:
- **Blur (mengaburkan)**.
- **Sharpening (penajaman)**.
- **Edge detection (pendeteksian tepi)**.
- 
**Contoh:**
```python
kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])  # Kernel Edge Detection
filtered_image = cv2.filter2D(image, -1, kernel)
```
---

### **3. Ekstraksi Ciri**
**Ekstraksi Ciri** adalah proses mendeteksi dan mengekstrak informasi penting dari citra, seperti:
- **Tepi** (Edges).
- **Titik Kunci** (Keypoints, seperti SIFT, ORB).
- **Histogram** (warna, tekstur).

**Tujuan**:
- Representasi data citra dalam bentuk yang lebih informatif dan efisien untuk digunakan pada tugas-tugas seperti pengenalan pola atau klasifikasi.

**Contoh:**
```python
sift = cv2.SIFT_create()
keypoints, descriptors = sift.detectAndCompute(image, None)
```
---
### **4. Evaluate Image Quality**
**Evaluasi Kualitas Citra** melibatkan pengukuran aspek tertentu pada citra, seperti:
- **Noise**: Tingkat gangguan (Gaussian, Speckle).
- **Sharpness**: Ketajaman citra.
- **Compression Artifacts**: Distorsi akibat kompresi (JPEG).
  
**Metode**:
- **PSNR (Peak Signal-to-Noise Ratio)**: Membandingkan citra asli dengan citra hasil pemrosesan.
- **SSIM (Structural Similarity Index)**: Mengevaluasi kesamaan struktur antara dua citra.

**Contoh:**
```python
psnr = cv2.PSNR(original_image, processed_image)
```
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
eroded_image = cv2.erode(binary_image, kernel, iterations=1)
```

---

### **6. Restorasi Citra**
**Restorasi Citra** adalah proses memperbaiki citra yang rusak akibat:
- **Noise**.
- **Blur**.
- **Artefak kompresi**.

**Metode**:
- **Deblurring**: Menghilangkan blur menggunakan deconvolution.
- **Denoising**: Mengurangi noise dengan filter seperti Gaussian atau Median.

**Contoh:**
```python
denoised_image = cv2.fastNlMeansDenoisingColored(color_image, None, 10, 10, 7, 21)
```
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
_, segmented_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
```
---

### **8. Transformasi Citra**
**Transformasi Citra** adalah operasi untuk memodifikasi posisi, orientasi, atau representasi citra. Contohnya:
- **Rotasi**: Memutar citra.
- **Scaling**: Mengubah ukuran citra.
- **Fourier Transform**: Mengubah domain citra menjadi domain frekuensi.

**Contoh:**
```python
# Rotasi
(h, w) = image.shape[:2]
M = cv2.getRotationMatrix2D((w // 2, h // 2), 45, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))
```
