import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)
# img = np.zeros([512, 512, 3], np.uint8) # Cria uma imagem em preto com numpy

img = cv2.line(img, (0, 0), (255, 255), (44, 147, 63), 10)  # Cria uma linha na imagem
# 1º argumento = A imagem escolhida
# 2° argumento = ponto 1
# 3° argumento = ponto 2
# 4° argumento = Cor
# 5° argumento = Espessura

img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)
# Cria a uma flecha na imagem

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 5)
# Cria um retangulo
# x1,y1 ------
# |          |
# |          |
# |          |
# ---------x2,y2

img = cv2.circle(img, (447, 63), 63, (0, 255, 0), 10)
# Cria um circulo

fonte = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Hello World!', (10, 500), fonte, 2, (255, 255, 255), 5, cv2.LINE_AA)
# Adiciona um texto la imagem

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
