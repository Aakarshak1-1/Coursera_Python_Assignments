from PIL import Image, ImageFilter
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")
blur = image.filter((ImageFilter.GaussianBlur(8)))
blur.show()
