# import PIL
from PIL import Image, ImageFilter

# load image
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105193934.jpg")

# apply effect using filter (kernel)
blurImage = image.filter(ImageFilter.GaussianBlur(10))

# display image
blurImage.show()
