## Datos recopilados y preprocesados para el análisis de discurso de odio en Panamá

Este repositorio contiene dos carpetas principales:

**1. Carpeta `data/`:**

* Almacena todos los datos sin procesar recopilados mediante técnicas de **webscraping**. La información recopilada se centra en **palabras clave, frases clave y temas de tendencia** relacionados con el discurso de odio en Panamá.

**2. Carpeta `preprocessed_data/`:**

* Contiene todos los datos **preprocesados** utilizando la herramienta **llama3**. Este proceso de preprocesamiento extrae información relevante para el análisis del discurso de odio, incluyendo:
    * Etiqueta de 'hate' o 'no hate': Indica si el texto contiene discurso de odio o no.
    * Breve explicación del contexto del post: Ofrece una descripción resumida del contexto en el que se publicó el texto.
    * Identificación de palabras ofensivas: Detecta y marca palabras que se consideran ofensivas o que se utilizan como insultos en el discurso de odio.

**2. Archivo `script.py`:**

* Script para ver la cantidad de datos en la carpeta data y juntar todos los datos en un solo archivo `all.csv`

* **

**Recursos adicionales:**

* **Código para ejecutar llama3:** [Llama3](https://colab.research.google.com/drive/1dTay-ZdNmIqIyc8zgXXK1skxaXdDdZ6G?usp=sharing)

* **Articulo HateSpeechIESTEC-2024, en proceso:** [Articulo](https://docs.google.com/document/d/19McUxY_-fNigmIuwXsC1xAypmN1LGX6h/edit?usp=sharing&ouid=109246043377937742676&rtpof=true&sd=true)
