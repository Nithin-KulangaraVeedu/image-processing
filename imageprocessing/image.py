from PIL import Image,ImageFilter

img = Image.open('./Pokedox/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert('L')
rotated_img = filtered_img.resize((100,100))
rotated_img.save("grey.png",'png')
rotated_img.show()
