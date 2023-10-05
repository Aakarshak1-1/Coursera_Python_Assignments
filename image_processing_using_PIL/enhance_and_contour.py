from PIL import Image, ImageFilter
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG-20200208-WA0063.bmp")
image = image.filter(ImageFilter.EDGE_ENHANCE)
image.show()
image = image.filter(ImageFilter.CONTOUR)
image.show()
