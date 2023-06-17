from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation

indices = []
for i in range(24):
        if i % 5 == 0:
            indices.append(i)
images = [
    Image.open(f'stacked/{ind}.png')
    for ind in indices
]

pdf_path = "bbd1.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)