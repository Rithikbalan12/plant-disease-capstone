from fastapi import FastAPI, File, UploadFile
from PIL import Image
import tensorflow as tf
import numpy as np
import json
import io

app = FastAPI(
    title="PlantCare AI API",
    description="Plant Disease Detection API",
    version="1.0.0"
)

model = tf.keras.models.load_model(
    "model/plant_disease_model.keras"
)

with open("model/class_names.json", "r") as f:
    class_names = json.load(f)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "message": "PlantCare AI API is running"
    }


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    image_bytes = await file.read()

    image = Image.open(
        io.BytesIO(image_bytes)
    ).convert("RGB")

    image = image.resize((224, 224))

    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
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