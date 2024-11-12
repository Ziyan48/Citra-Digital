import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters, img_as_ubyte, io

# Load the image in grayscale
img = cv2.imread('download.jpg', cv2.IMREAD_GRAYSCALE)

# Sobel Edge Detection
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = np.sqrt(sobelx**2 + sobely**2)

# Prewitt Edge Detection
kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
prewittx = cv2.filter2D(img, -1, kernelx)
prewitty = cv2.filter2D(img, -1, kernely)
prewitt = np.sqrt(prewittx**2 + prewitty**2)

# Roberts Edge Detection
robertsx = np.array([[1, 0], [0, -1]])
robertsy = np.array([[0, 1], [-1, 0]])
robertsx_img = cv2.filter2D(img, -1, robertsx)
robertsy_img = cv2.filter2D(img, -1, robertsy)
roberts = np.sqrt(robertsx_img**2 + robertsy_img**2)

# Laplacian of Gaussian (LoG)
blurred_img = cv2.GaussianBlur(img, (3, 3), 0)
log = cv2.Laplacian(blurred_img, cv2.CV_64F)
log = np.uint8(np.absolute(log))  # Ensure data type uint8

# Zero-Crossing Edge Detection
laplace = filters.laplace(io.imread('download.jpg', as_gray=True))

# Normalize laplace to be between 0 and 255 for uint8 compatibility
laplace_normalized = (laplace - laplace.min()) / (laplace.max() - laplace.min()) * 255
laplace_uint8 = laplace_normalized.astype(np.uint8)  # Convert to uint8
zero_crossing = filters.rank.minimum(laplace_uint8, np.ones((3, 3)))

# Canny Edge Detection
canny = cv2.Canny(img, 100, 200)

# Plotting all images
fig, axs = plt.subplots(2, 4, figsize=(20, 10))

# Display Original Image
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

# Sobel
axs[0, 1].imshow(sobel, cmap='gray')
axs[0, 1].set_title('Sobel Edge Detection')
axs[0, 1].axis('off')

# Prewitt
axs[0, 2].imshow(prewitt, cmap='gray')
axs[0, 2].set_title('Prewitt Edge Detection')
axs[0, 2].axis('off')

# Roberts
axs[0, 3].imshow(roberts, cmap='gray')
axs[0, 3].set_title('Roberts Edge Detection')
axs[0, 3].axis('off')

# Laplacian of Gaussian (LoG)
axs[1, 0].imshow(log, cmap='gray')
axs[1, 0].set_title('Laplacian of Gaussian (LoG)')
axs[1, 0].axis('off')

# Zero-Crossing
axs[1, 1].imshow(zero_crossing, cmap='gray')
axs[1, 1].set_title('Zero-Crossing Edge Detection')
axs[1, 1].axis('off')

# Canny
axs[1, 2].imshow(canny, cmap='gray')
axs[1, 2].set_title('Canny Edge Detection')
axs[1, 2].axis('off')

# Hide last subplot (since we have 6 methods)
axs[1, 3].axis('off')

# Show all images
plt.tight_layout()
plt.show()
