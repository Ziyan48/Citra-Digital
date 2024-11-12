#memilih warna biru saja pada gambar gambar 
import cv2 # menyertakan library cv2 dari opencv
import numpy as np

layar = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = layar.read()
    frame = cv2.flip(frame, 1)

    lowBlue = np.array([30, 10, 10])
    highBlue = np.array([40, 255, 255])
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    vidio = cv2.inRange(rgb, lowBlue, highBlue)
    
    
    cv2.imshow("vidio",vidio)

    if cv2.waitKey(1) == ord('q'):
        break

layar.release()
cv2.waitKey(0)
cv2.destroyAllWindows()