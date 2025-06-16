import streamlit as st
from PIL import Image
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms, models

# Dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Etiquetas de las clases
labels_classes = ["NonDemented", "VeryMildDemented", "MildDemented"]

# Transformaciones
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0, 0, 0], [1, 1, 1])
])

# MODELO 1: AlzheimerCNN
class AlzheimerCNN(nn.Module):
    def __init__(self, num_classes=3):
        super(AlzheimerCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
        self.conv2 = nn.Conv2d(32, 32, 3, padding=1)
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv3 = nn.Conv2d(32, 32, 3, padding=1)
        self.conv4 = nn.Conv2d(32, 32, 3, padding=1)
        self.pool2 = nn.MaxPool2d(2, 2)

        with torch.no_grad():
            dummy = torch.zeros(1, 3, 224, 224)
            x = self.pool1(F.relu(self.conv2(F.relu(self.conv1(dummy)))))
            x = self.pool2(F.relu(self.conv4(F.relu(self.conv3(x)))))
            self.flattened_size = x.view(1, -1).size(1)

        self.fc1 = nn.Linear(self.flattened_size, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, num_classes)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.pool1(x)
        x = F.relu(self.conv3(x))
        x = F.relu(self.conv4(x))
        x = self.pool2(x)
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        return self.fc3(x)

# MODELO 2: ResNet
class AlzheimerResNet(nn.Module):
    def __init__(self, num_classes=3):
        super(AlzheimerResNet, self).__init__()
        self.resnet = models.resnet18(pretrained=False)
        in_features = self.resnet.fc.in_features
        self.resnet.fc = nn.Linear(in_features, num_classes)

    def forward(self, x):
        return self.resnet(x)

# App de Streamlit
st.title("Clasificador de Alzheimer por Imágenes")
st.write("Sube una imagen y elige el modelo para predecir el grado de demencia")

# Botones para seleccionar modelo
model_choice = st.radio("Selecciona el modelo que quieres usar:", ("Sivaranjani-CNN", "ResNet18"))

uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Imagen cargada", use_column_width=True)

    img = transform(image).unsqueeze(0).to(device)

    # Cargar modelo según selección
    if model_choice == "Sivaranjani-CNN":
        model = AlzheimerCNN().to(device)
        weights_path = "3slicesPaper2Normalization01.pth"  # Cambia esto al path real
    else:
        model = AlzheimerResNet().to(device)
        weights_path = "3slicesResNetNormalization01.pth"  # Cambia esto al path real

    try:
        model.load_state_dict(torch.load(weights_path, map_location=device))
        model.eval()

        with torch.no_grad():
            output = model(img)
            probabilities = F.softmax(output, dim=1).cpu().numpy().flatten()

        st.subheader("Resultados de la predicción")
        for i, prob in enumerate(probabilities):
            st.write(f"{labels_classes[i]}: {prob*100:.2f}%")

    except Exception as e:
        st.error(f"Error al cargar los pesos del modelo: {e}")
