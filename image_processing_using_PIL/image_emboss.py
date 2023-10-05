from http.client import ImproperConnectionState
from PIL import Image, ImageFilter
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")
new_image = image.filter(ImageFilter.EMBOSS)
new_image.show()
