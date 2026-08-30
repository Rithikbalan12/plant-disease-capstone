from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import tensorflow as tf
import numpy as np
import json
import io
import os

app = FastAPI(
    title="PlantCare AI API",
    description="Plant Disease Detection API",
    version="1.0.0"
)

# Enable CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# LOAD MODEL
# =========================

model = tf.keras.models.load_model(
    "model/plant_disease_model.keras"
)

with open("model/class_names.json", "r") as f:
    class_names = json.load(f)


# =========================
# WEBSITE
# =========================

@app.get("/")
def home():
    index_path = os.path.join(
        os.path.dirname(__file__),
        "index.html"
    )

    return FileResponse(index_path)


# =========================
# HEALTH CHECK
# =========================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "message": "PlantCare AI API is running"
    }


# =========================
# PREDICTION
# =========================

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(
        io.BytesIO(image_bytes)
    ).convert("RGB")

    image = image.resize((224, 224))

    img_array = np.array(image)

    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    img_array = img_array / 255.0

    predictions = model.predict(
        img_array,
        verbose=0
    )

    predicted_index = int(
        np.argmax(predictions[0])
    )

    predicted_class = class_names[
        predicted_index
    ]

    confidence = float(
        predictions[0][predicted_index]
    ) * 100

    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 2)
    }