from PIL import Image, ImageFilter

# load image
image = Image.open(r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")

# apply effect
newImage = image.filter(ImageFilter.EMBOSS)

# display image
newImage.show()

