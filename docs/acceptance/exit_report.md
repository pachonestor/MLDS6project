 gil # Informe de salida

## Resumen Ejecutivo

## Resultados del proyecto

- En este proyecto se logro comprender la base de datos de la películas y extraer las características de la trama; con ellas generar 2 modelos de clasificación que entreguen la probabilidad de que según la trama de una película se logre dar porcentajes de que esa película pertenezca a ese género cinematografico. El modelo base fue una regresión logística y el modelo final fue una red neuronal. Además, se hizo un despliegue mediante FastAPI del modelo de clasificación, el cual se puede desplegar local medainte uvicorn e instalando ciertas librerias. Este despliegue recibe un archivo json con la trama de la película y entrega las probabilidades de que la trama pertezca a 23 géneros cinematograficos.
  
- En cuanto desempeño, el modelo base tiene roc auc con promedio macro  y multiclase uno vs el resto de clases puntaje de 0.767 mientras que el modelo final un puntaje de 0.805. Cabe resaltar que para la evaluación de ambos modelos se quito el généro de News por ser muy pequeño, ya que solo contaba con 7 instancias y  además cada vez que aparecia en una clase también se encontraba el género Documentary, por lo que no se perdia información relevante del modelo al quitarlo.
  
- Así mismo, como el roc auc fue mejor en la red neuronal que la regresión logística, tambíen lo fueron los F1 score de cada una de las clases ya que la clase que mejor se clasificó en la regresión fue la Documentary con un F1 Score de 0.29 y la peor fue Short con 0.03, mientras que la red neuronal tuvo como mejor puntaje el género de Sport con 0.41 y como peor puntaje Short con 0.0. Por otro lado, casi todas las clases tuvieron tuvieron mejor puntaje con la red neuronal que con la regresión logística excepción de la Comedia, Música y Músical donde fue ligeramente deficiente y esto se muestra en la siguiente tabla.



| Modelo Base   | Modelo Final  |
| -------- | ------------- |
| ![base_class_report](images/base_class_report.png)  | ![main_class_report](images/main_class_report.png) | 


  

## Lecciones aprendidas

- Los principales retos en este proyecto fueron 2, el problema de clasificación en sí, al ser de clases desbalanceadas, complico el entrenamiento de los modelos y la corta duración del proyecto impidio una investigación y búsqueda de modelos, preprocesamiento y embbeding más exhastiva.
- Con respecto al modelamiento, se pudo haber hecho un análisis de cluster para agrupar varias clases en un grupos de significado similar, y con ello obtener mayor número de datos y clases ḿas balancedas haciendo más interpretable y fácil el entremaniento el modelo de clasificación.

## Impacto del proyecto

- El modelo ayuda a automatizar el etiquetado de películas según el género al que pertenece haciendo más ágil la documentación de nuevas películas ahoprrando tiempo.
- Se puede mejorar el modelo utílizando embeddings ya entrenados que sacan una representación más interpretativa de los datos.
- Del mismo modo, se puede implementar la agrupación de clases con el fin de mejorar la precisión del modelo caracterizar mejor los géneros del cine.

## Conclusiones

- El modelo se puede desplegar en local, es útil
- Conclusiones finales y recomendaciones para futuros proyectos.

## Agradecimientos

- Agradecimientos al equipo de trabajo y a los colaboradores que hicieron posible este proyecto.
- Agradecimientos especiales a los patrocinadores y financiadores del proyecto.
