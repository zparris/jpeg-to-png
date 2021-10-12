from PIL import Image, ImageFilter

img = Image.open('./profile_pic.jpeg')
img.thumbnail((400, 200))
img.save('thumbnail.jpeg')

print(img.size)

