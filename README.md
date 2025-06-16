# Clasificación de Imágenes MRI para Diagnóstico de Demencia

Este proyecto implementa un sistema de clasificación de imágenes por resonancia magnética cerebral (MRI) con el fin de estimar el grado de demencia. Se basa en redes neuronales convolucionales, incluyendo varias arquitecturas personalizadas de artículos (como Sivaranjani-CNN) y arquitecturas de IMagenet (ResNet18, MobileNet y AlexNet).

## 📁 Estructura del Proyecto

├── interfaz/ # Interfaz web con Streamlit<br>
│ ├── app.py # Aplicación principal Streamlit<br>
│ ├── *.png # Imágenes de ejemplo<br>
│ └── *.pth # Pesos preentrenados de los modelos de interfaz<br>
├── requirements.txt # Lista de dependencias de Python<br>
├── setup.py # Script para descarga y preparación de datos<br>
└── modelos/ # carpeta con las versiones<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── version */ # Imágenes de ejemplo<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── *.ipynb # Jupiter Notebooks con el codigo de los modelos entrenados<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└──*.pth # Pesos preentrenados de los modelos<br>

---

## ⚙️ Requisitos

- Python 3.7 o superior
- [pip](https://pip.pypa.io/)
- Conexión a Internet para la descarga de datos
- Navegador moderno para usar la interfaz web (Chrome, Firefox, etc.)

---

## 🛠️ Instalación

1. **Clona el repositorio** :

```bash
  git clone  https://github.com/martacuevasr/Clasification_AlzheimerImages.git
  cd Clasification_AlzheimerImages
```

2. **Crea un entorno virtual (recomendado)**:

```bash
  python -m venv venv
  # Activar entorno en Linux/macOS
  source venv/bin/activate
  # Activar entorno en Windows
  venv\Scripts\activate
```
3.**Instala las dependencias**:

```bash
  pip install -r requirements.txt
```

## 📥 Descarga y Preparación de Datos

Ejecuta el siguiente script para descargar, descomprimir y organizar el conjunto de datos necesario:

```bash
python setup_data.py
```

Este script realiza las siguientes acciones:

- 📥 Descarga los datos desde la fuente indicada.
- 📦 Descomprime los archivos.
- 📂 Crea la estructura de carpetas para imágenes y anotaciones.

---

## 🧠 Modelos Disponibles

Los siguientes modelos están incluidos y se encuentran en la carpeta `interfaz/`:

- `3slicesPaper2Normalization01.pth`: modelo **Sivaranjani-CNN**
- `3slicesResNetNormalization01.pth`: modelo **ResNet18**

## 🖥️ Interfaz Web

Para lanzar la aplicación de predicción mediante Streamlit:

´´´bash
cd interfaz
streamlit run app.py
´´´

## 🖥️ Interfaz Web

La interfaz permite:

- Cargar una imagen MRI en formato **JPG, JPEG o PNG**.
- Seleccionar el modelo (**Sivaranjani-CNN** o **ResNet18**).
- Obtener la **predicción de probabilidades** para cada clase de demencia (leve, moderada, severa...).

> ⚠️ **Importante:** Asegúrate de que los archivos `.pth` con los pesos estén en la misma carpeta que `app.py`, o en la ruta especificada en el código.



