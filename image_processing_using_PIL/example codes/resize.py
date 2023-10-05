# Import module
from PIL import Image

# Load image from disk
im = Image.open(r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG20220105162858.jpg")

# Resize image
im = im.resize(100,100)

# Show image
im.show()
