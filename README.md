* En la carpera de Code se encuentra los codigos:

training.ipynb ----> Modelo que carga, preprocesa, entrena, valida y guarda el modelo
exercise.py ----> Este codigo contiene el endpoint de fastapi para las consultas del modelo
requirements.txt ---> Requerimientos de instalacion del modelo
fashion_mnist_model.keras ---> Pesos del modelo entrenado
Dockerfile

* En la carpera de images se encuentra el codigo para guardar imagenes del dataset y facilitar la consulta por http

* En la carpeta quipux se encuentra el env 

Antes de correr el codigo, asegurese de activar el entorno virtual llamado quipux:

cd .\quipux\     
.\Scripts\activate

Cuando este activado podra acceder a la carpera Code y correr el dockerfile:

docker build -t fashion_model_quipux .  
docker run -p 8000:8000 fashion_model_quipux  

Luego de esto, podra hacer las consultas en el endpoint a partir de:
http://localhost:8000/docs
