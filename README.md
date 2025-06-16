# Clasificación de Imágenes MRI para Diagnóstico de Demencia

Este proyecto implementa un sistema de clasificación de imágenes por resonancia magnética cerebral (MRI) con el fin de estimar el grado de demencia. Se basa en redes neuronales convolucionales, incluyendo varias arquitecturas personalizadas de artículos (como Sivaranjani-CNN) y arquitecturas de IMagenet (ResNet18, MobileNet y AlexNet).

## 📁 Estructura del Proyecto
├── interfaz/ # Interfaz web con Streamlit
│ ├── app.py # Aplicación principal Streamlit
│ ├── *.png # Imágenes de ejemplo
│ └── *.pth # Pesos preentrenados de los modelos de interfaz
├── requirements.txt # Lista de dependencias de Python
├── setup.py # Script para descarga y preparación de datos
└── modelos/ # carpeta con las versiones
│ └── version*/ # Imágenes de ejemplo
│   │    ├── *.ipynb # Jupiter Notebooks con el codigo de los modelos entrenados
└── └──  └── *.pth # Pesos preentrenados de los modelos

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

##📥 Descarga y Preparación de Datos
Ejecuta el siguiente script para descargar, descomprimir y organizar el conjunto de datos necesario:



