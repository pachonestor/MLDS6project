# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Clasificación de géneros cinematograficos según la trama de una película.
- **Plataforma de despliegue:** El modelo será desplegado en un servidor local usando uvicorn como método de apretura de puertos.
- **Requisitos técnicos:** 
    - *versión de Python:* python 3.10.11
    - *Librerias:* fastapi(0.98.0), fastjsonschema(2.15.3), jsonschema(4.5.1),python-lsp-jsonrpc(1.0.0), ujson(5.3.0), numpy(1.23.5), tensorflow(2.12.0),tensorflow-estimator(2.12.0),
      joblib(1.2.0), keras(2.12.0), nltk(3.8.1), pandas(2.0.2), python-multipart(0.0.6), regex(2023.6.3), scikit-learn(1.2.2),spacy(3.5.3), unidecode(1.3.6), uvicorn(0.22.0), tempfile
    - *Software:* Ubuntu 16.04.7 LTS(X86_64)
    - *Hardware:* CPU: Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz, GPU: None, RAM: 5,7 GiB
- **Requisitos de seguridad:** Al tratarse de datos de resumenes de películas que están disponibles al  público no hay necesidad
- **Diagrama de arquitectura:**

![tcga_example](images/Arquitectura.png)

## Código de despliegue

- **Archivo principal:** La aplicación diseñada está en el archivo *deploymentAPIs.py*
- **Rutas de acceso a los archivos:** El código puede encontrarse en *'src/nombre_paquete/deployment/deploymentAPIs.py'*

## Documentación del despliegue

- **Instrucciones de instalación:** Debe considerar la instalación de los paquetes asociados a openslide como a NVIDIA (CUDA, CUDNN). El resto de librerías mencionadas puede obtenerse por medio de pip. 
- **Instrucciones de configuración:** La mayoría de hiperparametros del modelo han sido explorados previamente y por consiguiente no se recomienda ninguna modificación sobre estos.
- **Instrucciones de uso:** El despliegue del modelo consta de dos pasos
    - *Despliegue del servidor:* Se pone en producción la aplicación creada, para ello ejecutar.
          - uvicorn {main_file_path}:app --reload 
    - *Apertura de puertos:* Para poder tener acceso a nuestro servicio desde cualquier punto debemos abrir el 8000, no obstante esto se encuentran normalmente restringidos por nuestro operado de internet, para evadir dichas limitaciones usamos el servicio de ngrok.
          - ./MLDS6project/src/nombre_paquete/preprocessing/ngrok http 8000
