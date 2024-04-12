from PIL import Image

# Script 1 - Convert jpgs to pngs

open_image = Image.open('../grogu.jpg')
open_image.save('grogu.png')

# Script 2 - Convert images to a set resolution

converted_image = Image.open('grogu.png')
size = 1280, 1024
resized = converted_image.resize(size, Image.Resampling.NEAREST)
resized.save("grogu_resized.png")
