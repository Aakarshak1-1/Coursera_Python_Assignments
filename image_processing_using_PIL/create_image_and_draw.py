from PIL import Image, ImageColor, ImageDraw
# create image
image = Image.new("RGB", (1000, 700), ImageColor.getrgb("#ffffff"))
# darw line
draw = ImageDraw.Draw(image)
draw.line([(0, 0), (1000, 700)], fill='red', width=5)
# draw circle
draw.ellipse((50, 100, 150, 200), fill='blue', outline=(0, 0, 0,))
# draw rectangle
draw.rectangle((200, 100, 300, 200), fill='green', outline=(255, 0, 0))
# display image
image.show()
