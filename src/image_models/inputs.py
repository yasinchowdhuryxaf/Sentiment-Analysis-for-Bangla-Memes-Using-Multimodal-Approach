"""Image input demonstration, not CNN training or inference."""
from PIL import Image

def load_rgb_image(path, size=(224, 224)):
    with Image.open(path) as image:
        return image.convert("RGB").resize(size, Image.Resampling.BILINEAR)
