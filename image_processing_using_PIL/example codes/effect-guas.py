from PIL import Image, ImageFilter

# load image
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")

# apply effect
blurImage = image.filter(ImageFilter.GaussianBlur(7))

# display image
blurImage.show()
