import cv2
import numpy as np
import argparse
import imutils

def process_image(image_path):
    # Membaca gambar dan merubah ukuran
    gambar1 = cv2.imread(image_path)
    gambar1 = cv2.resize(gambar1, (400, 400))

    # Konversi gambar ke grayscale dan blurring
    gray = cv2.cvtColor(gambar1, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding untuk menghasilkan gambar biner
    _, BW1 = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

    # Deteksi tepi dengan Canny pada gambar biner
    edges = cv2.Canny(blurred, 100, 100)

    # Temukan kontur pada gambar hasil Canny
    cnts = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Buat salinan gambar asli untuk ditampilkan dengan label kontur
    labeled_image = gambar1.copy()
    canny_with_labels = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Loop untuk setiap kontur yang terdeteksi
    for c in cnts:
        # Hitung momen untuk menemukan pusat kontur, cek jika area (m00) tidak nol
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            # Hitung keliling dan area kontur
            perimeter = cv2.arcLength(c, True)
            area = cv2.contourArea(c)
            
            # Rasio kebulatan
            circularity = (4 * np.pi * area) / (perimeter * perimeter) if perimeter > 0 else 0
            
            # Tentukan apakah bulat atau tidak bulat
            label = "Bulat" if 0.8 <= circularity <= 1.2 else "Tidak Bulat"
            
            # Gambar kontur dan pusat pada gambar asli
            cv2.drawContours(labeled_image, [c], -1, (0, 0, 255), 1)
            cv2.circle(labeled_image, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(labeled_image, label, (cX - 20, cY - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            cv2.drawContours(canny_with_labels, [c], -1, (0, 0, 255), 1)
            # cv2.circle(canny_with_labels, (cX, cY), 7, (255, 255, 255), -1)
            # cv2.putText(canny_with_labels, label, (cX - 20, cY - 20),
            #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Tampilkan gambar asli dengan label kontur
    cv2.imshow(f"Labeled Image - {image_path}", labeled_image)
    cv2.imshow(f"Canny Labeled Image - {image_path}", canny_with_labels)

# Inisialisasi argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", nargs='+', default=["bidang.png", "satelit2.png"], help="paths to the input images")
args = vars(ap.parse_args())

# Proses setiap gambar
for image_path in args["images"]:
    process_image(image_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
