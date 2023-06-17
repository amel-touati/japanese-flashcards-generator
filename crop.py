from PIL import Image

image = Image.open(f'output/{1}.png')
width, height = image.size


# Calculate the coordinates for cropping
left = 0
top = 0
right = width - 280
bottom = height - 120

# Open the image
for ind in range(125):
    image = Image.open(f'output/{ind}.png')
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(f'flashcards/{ind}.png')