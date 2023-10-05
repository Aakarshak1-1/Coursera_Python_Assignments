from PIL import Image

# load image
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")
dog = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105193934.jpg")
image.show()

# crop
# box=(left,top,right,bottom)
box = (100, 188, 547, 591)
croppedImg = image.crop(box)
croppedImg.show()

# paste
image.paste(croppedImg, (447, 400))
image.paste(dog, (0, 0))
image.paste(croppedImg, (0, 400))
image.show()
