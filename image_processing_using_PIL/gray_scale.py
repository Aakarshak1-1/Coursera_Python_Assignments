from PIL import Image, ImageOps
im1 = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\farewell\IMG-20200208-WA0063.jpg")
im2 = ImageOps.grayscale(im1)
im2.show()
