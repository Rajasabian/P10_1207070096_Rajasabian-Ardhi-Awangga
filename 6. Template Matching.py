# tampilkan kedua gambar
from matplotlib import pyplot as plt
import cv2
# panggil dan konversi warna agar sesuai dengan Matplotlib
img = cv2.imread('mukaraja.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # simpan dengan nama yang sama = ditumpuk
# panggil dan konversi warna agar sesuai dengan Matplotlib
futsal = cv2.imread('futsal.jpg')
futsal = cv2.cvtColor(futsal, cv2.COLOR_BGR2RGB) 
plt.subplot(121),plt.imshow(img), plt.title('mukaraja')
plt.subplot(122),plt.imshow(futsal), plt.title('futsal')
plt.show()