from PIL import Image
from PIL import Image

# Create an Image Object from an Image
im = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")

# Display actual image
im.show()

# Make the new image half the width and half the height of the original image
resized_im = im.resize((round(im.size[0]*0.1), round(im.size[1]*0.1)))

# Display the resized imaged
resized_im.show()
