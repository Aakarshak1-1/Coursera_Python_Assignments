from PIL import Image
image_1 = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105193934.jpg")
image_2 = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")
# crop
box = (70, 80, 500, 500)
cropped_image = image_1.crop(box)
cropped_image.save('cropped_image.jpg')
# paste
image_2.paste(cropped_image, (100, 500))
image_2.show()
