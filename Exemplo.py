import cv2

# Recordar placa da imagem

img = cv2.imread('resource/carro (1).jpg')
# img = cv2.imread('resource/teste_1.jpg')
# img = cv2.imread('resource/teste_2.jpg')
cv2.imshow('img', img)

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('cinza', cinza)

# Binarizar imagem. Limite minimo preto e máximo branco. Precisa estar na escala de cinza a imagem indicada no parametro
_, bin = cv2.threshold(cinza, 90, 255, cv2.THRESH_BINARY)
# cv2.imshow('bin', bin)

desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
# cv2.imshow('desfoque', desfoque)

# RETR_TREE: Busca completa, pesquisar contorno dentro de contorno
contornos = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[0]
# print(contornos)

# cv2.drawContours(img, contornos, -1, (0, 255, 0), 1)
# cv2.imshow('contornos', img)

for c in contornos:
    perimetro = cv2.arcLength(c, True)
    if perimetro > 120: # Eliminar retangulos pequenos
        aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True) # Aproximar da forma geométrica mais proxima (circulo, retanguo, quadrado, triangulo, poligonos)
        if len(aprox) == 4: # Se a forma geométrica aproxima possuir 4 pontos (retangulo ou quadrado)
            (x, y, lar, alt) = cv2.boundingRect(c) # Transformar num retangulo
            cv2.rectangle(img, (x, y), (x + lar, y + alt), (0, 255, 0), 1)
            roi = img[y:y + alt, x:x + lar]
            cv2.imwrite('output/placa.jpg', roi)

cv2.imshow('contornos', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("OK")