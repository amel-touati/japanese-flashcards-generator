from PIL import Image

ind = 0
page = 3

for _ in range(85):
    image1 = Image.open(f'flashcards/{ind}.png')
    image2 = Image.open(f'flashcards/{ind+1}.png')
    image3 = Image.open(f'flashcards/{ind+2}.png')
    image4 = Image.open(f'flashcards/{ind+3}.png')
    output_width = max(image1.width, image2.width, image3.width, image4.width)
    output_height = sum([image1.height, image2.height, image3.height, image4.height])
    output_image = Image.new('RGB', (output_width, output_height))
    y_offset = 0
    output_image.paste(image1, (0, y_offset))
    y_offset += image1.height
    output_image.paste(image2, (0, y_offset))
    y_offset += image2.height
    output_image.paste(image3, (0, y_offset))
    y_offset += image3.height
    output_image.paste(image4, (0, y_offset))

    # Save the final output image
    output_image.save(f'stacked/{page}.png')
    page = page + 1
    ind = ind + 4