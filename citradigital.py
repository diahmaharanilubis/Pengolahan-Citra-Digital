import cv2
import os

# Gunakan jalur file yang benar
file_path = 'hias.jpg'  # Gantilah dengan jalur gambar Anda

# Periksa apakah file ada di jalur yang diberikan
if not os.path.exists(file_path):
    print(f"Gambar tidak ditemukan di jalur: {file_path}")
    exit()

# Baca gambar RGB
img = cv2.imread(file_path)

# Periksa apakah gambar berhasil dibaca
if img is None:
    print("Gambar tidak dapat dibaca, periksa kembali jalur file!")
    exit()

# Ubah gambar ke grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Buat gambar merah dan biru
red_image = img.copy()
blue_image = img.copy()

# Set channel selain merah ke 0 untuk red_image
red_image[:, :, 0] = 0  # Set kanal biru ke 0
red_image[:, :, 1] = 0  # Set kanal hijau ke 0

# Set channel selain biru ke 0 untuk blue_image
blue_image[:, :, 1] = 0  # Set kanal hijau ke 0
blue_image[:, :, 2] = 0  # Set kanal merah ke 0

# Simpan gambar grayscale, merah, dan biru
cv2.imwrite('grayscale_image.jpg', gray_image)
cv2.imwrite('red_image.jpg', red_image)
cv2.imwrite('blue_image.jpg', blue_image)

# Tampilkan gambar asli, grayscale, merah, dan biru
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray_image)
cv2.imshow('Red Image', red_image)
cv2.imshow('Blue Image', blue_image)

# Tunggu sampai ada tombol yang ditekan
cv2.waitKey(0)
cv2.destroyAllWindows()
