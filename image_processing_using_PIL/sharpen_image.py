from PIL import Image, ImageFilter
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG-20200208-WA0063.bmp")
image.show()
image = image.filter(ImageFilter.SHARPEN)
image.show()
