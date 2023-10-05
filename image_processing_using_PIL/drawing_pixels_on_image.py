from PIL import Image, ImageColor, ImageDraw
image = Image.new("RGB", (700, 700), ImageColor.getrgb("#ffffff"))
width, height = image.size

for x in range(height):
    image.putpixel((x, x), (255, 55, 255, 255))
    image.putpixel((x, -x), (255, 0, 255, 255))
    image.putpixel((x, 100), (255, 0, 0, 255))
image.show()
