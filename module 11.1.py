# Библиотека Pillow

from PIL import Image

# открытие изображения
im1 = Image.open('IMG_0369.jpg')
im2 = Image.open("me.jpg")

# узнаем формат, размеры и цветовую гамму
print(im1.format, im1.size, im1.mode)
print(im2.format, im2.size, im2.mode)

# поворот изображения
im2 = im2.transpose(Image.Transpose.ROTATE_270)


# обработка изображения (изменение цвета, размера)
def new_foto(new_image):
    w, h = new_image.size
    new_image = new_image.resize((w // 2, h // 2))
    new_image = new_image.convert('L')
    return new_image


# создание нового фото путем соединения нескольких
def merge(im1, im2, im3):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new("RGBA", (w, h))
    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    im.paste(im3, (0, 1200))
    return im


im1 = new_foto(im1)
im2 = new_foto(im2)
im3 = Image.open('hi.png')
im = merge(im1, im2, im3)
im.show()