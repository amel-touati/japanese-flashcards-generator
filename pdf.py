from PIL import Image

indices = list(range(1, 21))
images = [
    Image.open(f'stacked/{ind}.png').convert('RGB')
    for ind in indices
]

pdf_path = "bbd1.pdf"

images[0].save(
    pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
