# Reporte del Modelo Baseline

## Descripción del modelo

El de base es un Random Forest, que toma como variables de entrada la matriz generada por el embedding TfidfVectorizer del las reseñas de la trama de peliculas y como salida un vector de los 23 géneros de cinemátograficos en formato dummies

## Variables de entrada

Son 280 variables extraidas del las tramas mediante el embedding TfidfVectorizer; las palabras que se selecciionaron de tal manera que estuviera en 95% de las tramas de las películas y como mínimo en un 3% de ellas.

Además, para mejorar la precisión del modeloy debido a la presentación de los datos, se genero un registro por cada généro que tuviera la película,ya que hay películas con más de un género

## Variable objetivo

Los genéros cinematográficos de las películas en formato multiclase.

## Evaluación del modelo

### Métricas de evaluación

La métrica ROC AUC (Área bajo la curva ROC) se utiliza para evaluar el rendimiento de un modelo en problemas de clasificación. En el caso de clasificación multiclase, donde se tienen más de dos clases, se puede utilizar el enfoque "average macro" para calcular la métrica ROC AUC.

En el enfoque "average macro", se calcula la curva ROC y el área bajo ella para cada clase individualmente. Luego, se toma el promedio de estas áreas para obtener el valor final del ROC AUC. Esto significa que se trata cada clase por igual y se promedia su rendimiento individual.

La curva ROC representa la tasa de verdaderos positivos (TPR) en función de la tasa de falsos positivos (FPR). Para cada clase, el modelo establece un umbral de probabilidad para decidir la clasificación, y se calcula el TPR y el FPR correspondientes para ese umbral. El área bajo la curva ROC es una medida de la capacidad del modelo para distinguir entre clases positivas y negativas.

En el enfoque "average macro", todas las clases tienen el mismo peso y se promedia su rendimiento individual. Esto es útil cuando se desea evaluar el rendimiento general del modelo en todas las clases de manera equitativa, sin importar si algunas clases tienen más muestras que otras. Sin embargo, es importante tener en cuenta que el enfoque "average macro" puede ocultar desequilibrios en el rendimiento de las clases individuales.

### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora.

## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Espero que te sea útil esta plantilla. Recuerda que puedes adaptarla a las necesidades específicas de tu proyecto.
