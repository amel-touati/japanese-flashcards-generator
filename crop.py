from PIL import Image

for ind in range(76):
    image = Image.open(f'output/{ind}.png')
    width, height = image.size

    # Calculate the coordinates for cropping
    crop_width = 150  # Adjust this value as needed
    left = crop_width
    top = 0
    right = width - crop_width
    bottom = height - 108

    # Perform cropping
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(f'flashcards/{ind}.png')
