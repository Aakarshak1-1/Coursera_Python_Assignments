from PIL import Image, ImageFont, ImageDraw
image = Image.open(
    r"C:\Users\shotr\OneDrive\Pictures\Haridwar\IMG-20200208-WA0063.bmp")
draw = ImageDraw.Draw(image)
my_font = ImageFont.truetype(
    r"C:\Users\shotr\Downloads\arduino-nightly-windows\arduino-nightly\java\lib\fonts\LucidaBrightItalic.ttf", 40)
text = "Hard Work \n beats talent"

draw.text((250, 200), text, font=my_font, fill=(255, 0, 0))
image.show()
