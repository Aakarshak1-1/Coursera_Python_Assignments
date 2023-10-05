from PIL import Image
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")

i = 0
while(i != 405):
    print(i)
    image = image.rotate(i, expand=True)
    image.show()
    i = i+45
