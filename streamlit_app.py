import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import json

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱"
)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        "model/plant_disease_model.keras"
    )

@st.cache_data
def load_class_names():
    with open("model/class_names.json", "r") as f:
        return json.load(f)

model = load_model()
class_names = load_class_names()

st.title("🌱 PlantCare AI")
st.subheader("Plant Disease Detection")

st.write(
    "Upload a plant leaf image and let AI detect the disease."
)

uploaded_file = st.file_uploader(
    "Choose a leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Leaf Image",
        use_container_width=True
    )

    if st.button("🔍 Predict Disease"):

        image_resized = image.resize((224, 224))

        img_array = np.array(image_resized)
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

        confidence = (
            float(predictions[0][predicted_index])
            * 100
        )

        st.success(
            f"Prediction: {predicted_class}"
        )

        st.info(
            f"Confidence: {confidence:.2f}%"
        )