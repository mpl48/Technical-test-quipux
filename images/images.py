import tensorflow as tf
import numpy as np
from PIL import Image

# Descargar el conjunto de datos Fashion MNIST
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Función para guardar una imagen en un archivo
def save_image(image_array, file_path):
    image = Image.fromarray(image_array)
    image.save(file_path)

# Guardar algunas imágenes de ejemplo
for i in range(10):
    file_path = f"fashion_mnist_image_{i}.png"
    save_image(train_images[i], file_path)