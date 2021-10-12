import glob
import sys
# to grab first and second argument
import os
# to grab path
from PIL import Image


# Grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create
if not os.path.exists(output_folder):
	os.makedirs(output_folder)


filename = [f for f in glob.glob(image_folder+'*.jpg')]  # or .png, .tif, etc

# loop through Pokedex,
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]

	img.save(f'{output_folder}{clean_name}.png', 'png')
	print('all done!')

# convert to png

# save to new folder