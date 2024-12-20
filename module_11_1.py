# Библиотека обработки изображений добавляет возможности обработки изображений в интерпретатор Python
from PIL import Image, ImageOps

im1 = Image.open("Moscow-1.jpg")
im2 = Image.open("Moscow-2.jpg")
im3 = Image.open("Moscow-3.jpg")

print(im1.format, im1.size, im1.mode)
print(im2.format, im2.size, im2.mode)
print(im3.format, im3.size, im3.mode)

im1.show() # Показать изображение стандартным редактором изображений

im2.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save("Moscow-2_trans_lr.jpg") # Транспонирование лево-право

ImageOps.fit(im3,(400, 600)).save("Moscow-3_fit.jpg") # Обрезка изображения по размерам
ImageOps.contain(im1, (500, 800)).save("Moscow-1_contain.png") # Вписывание изображение в заданные размеры по горизонтале, сохраняя соотношение сторон
ImageOps.cover(im2, (600, 800)).save("Moscow-2_cover.bmp") # Вписывание изображение в заданные размеры по вертикале, сохраняя соотношение сторон
ImageOps.pad(im3, (400, 400), color="#f00").save("Moscow-3_pad.tiff") # Изменение размера и дополнение изображения до заданных размеров

im1.convert("L").save("Moscow-1_bw.jpg") # преобразование изображения в черно-белое (8-бит серого)
