from PIL import Image, ImageOps
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG-20200208-WA0063.bmp")
image.show()
# Flip vertically

image = ImageOps.flip(image)
image.show()

# Flip Horizontally

image = ImageOps.mirror(image)

# GrayScale
image = ImageOps.grayscale(image)
image.show()
