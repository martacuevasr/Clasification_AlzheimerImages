
import os
import kagglehub

def create_directories():
    print("Creando estructura de carpetas...")
    os.makedirs("data", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    print("Carpetas listas.")

def download_dataset():
    print("Descargando el dataset de Kaggle...")
    try:
        dataset_path = kagglehub.dataset_download("yiweilu2033/well-documented-alzheimers-dataset")
        print(f"Dataset descargado en: {dataset_path}")
        return dataset_path
    except Exception as e:
        print("Error al descargar el dataset:")
        print(e)

if __name__ == "__main__":
    create_directories()
    dataset_dir = download_dataset()
    print("Setup completo.")
