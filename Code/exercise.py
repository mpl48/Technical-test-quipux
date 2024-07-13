from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import io
import tensorflow as tf

app = FastAPI()
model = tf.keras.models.load_model('fashion_mnist_model.keras')

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

@app.post("/process_image/")
async def process_image(file: UploadFile = File(...)):
    # Leer el archivo subido en bytes
    image_bytes = await file.read()

    # Convertir bytes a imagen usando PIL
    image = Image.open(io.BytesIO(image_bytes))

    # Convertir la imagen a un array numpy
    image_array = np.array(image.convert('L'))  # Convertir a escala de grises si es necesario

    # Preprocesar la imagen
    img = image_array.reshape(1, 28, 28, 1) / 255.0

    # Hacer la predicción
    prediction = model.predict(img)

    # Obtener la etiqueta con la mayor probabilidad
    predicted_class = np.argmax(prediction)
    predicted_label = class_names[predicted_class]

    return {"prediction": predicted_label}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
