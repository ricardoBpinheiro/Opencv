import cv2

img = cv2.imread('lena.jpg', 1)
# .imread('imagem', 1)
# -1 = Unchanged image
# 0 = grayscale
# 1 = color

print(img)

cv2.imshow('image', img)  # Mostra a imagem em um box
k = cv2.waitKey(0) & 0xFF    # deixa a imagem aberta no tempo informado

if k == 27:  # Se aperta k fecha a imagem
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)  # Cria uma copia da imagem
    cv2.destroyAllWindows()
