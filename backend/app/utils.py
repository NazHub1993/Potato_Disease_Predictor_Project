import numpy as np
from PIL import Image
from .config import IMAGE_SIZE


def preprocess_image(image: Image.Image):
    image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    image = np.array(image) / 255.0
    return image.tolist()
