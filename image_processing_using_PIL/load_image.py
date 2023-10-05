from PIL import Image, ImageOps
# create image
im1 = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\farewell\IMG-20200208-WA0063.jpg")
# show image
im1.show()
# invert image
im3 = ImageOps.invert(im1)
im3.show()
