from PIL import Image
im = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")
print(im.format)
print(im.mode)
print(im.size)
print(im.height)
print(im.width)
# print(im.info)
im.show()
