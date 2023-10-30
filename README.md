# README - Proyecto de Clasificación de Textos (Machine Learning)

Este proyecto tiene como objetivo desarrollar un sistema de clasificación de textos utilizando técnicas de Procesamiento de Lenguaje Natural (NLP) y Machine Learning. El sistema clasificará los textos en categorías de objetivos de desarrollo sostenibles (ONU).

## Requisitos

Asegúrate de tener instalados los siguientes paquetes y bibliotecas:

- Python 3.x
- Bibliotecas de Python (numpy, pandas, scikit-learn, flask, spacy, etc.)

## Configuración

1. Clona este repositorio en tu máquina local.
2. Instala las bibliotecas y paquetes necesarios utilizando `pip`.
3. Asegúrate de tener un entorno virtual configurado y activado para evitar conflictos de paquetes.
4. Descarga e instala el modelo de lenguaje de spaCy para el idioma español:

```bash
python -m spacy download es_core_news_sm
```

## Uso

- Ejecuta el archivo `app.py` para iniciar la aplicación web.
- Accede a la interfaz de usuario desde tu navegador en `http://localhost:5000`.
- Sube un archivo de texto en español para clasificar.
- Visualiza los resultados de la clasificación en la pantalla.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación web.
- `pipelines.py`: Contiene la definición y entrenamiento de los pipelines de procesamiento y modelos de Machine Learning.
- `templates`: Carpeta que contiene los archivos HTML para la interfaz de usuario.
- `static`: Carpeta para archivos estáticos como imágenes y estilos CSS.
- Otros archivos y carpetas necesarios para el proyecto.

## Contribuir

Si deseas contribuir a este proyecto, no dudes en realizar una solicitud de extracción (Pull Request) con tus mejoras.

## Licencia

Este proyecto es resultado de la materia Inteligencia de negocios de la Universidad de los Andes. Por el momento no tiene licencia pero la universidad es el segundo agente dueño de este mismo.

## Contacto

Para cualquier pregunta o sugerencia, puedes contactarme en j.coronel@uniandes.edu.co.

---

¡Gracias por tu interés en este proyecto!
