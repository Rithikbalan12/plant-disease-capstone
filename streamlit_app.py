import streamlit as st
import requests
from PIL import Image
import io

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="PlantCare AI",
    page_icon="🌱",
    layout="centered"
)

# =========================================================
# FASTAPI BACKEND URL
# =========================================================

import os

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)


# =========================================================
# HEADER
# =========================================================

st.title("🌱 PlantCare AI")
st.subheader("Plant Disease Detection")

st.write(
    "Upload a plant leaf image and let AI detect the disease."
)


# =========================================================
# HEALTH CHECK
# =========================================================

def check_backend_health():
    """Check if the FastAPI backend is running."""
    try:
        response = requests.get(
            f"{API_URL}/health",
            timeout=5
        )
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


# =========================================================
# FILE UPLOADER
# =========================================================

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

        # Check backend health first
        if not check_backend_health():
            st.error(
                "Backend API is not available. "
                "Please make sure the FastAPI server "
                "is running on " + API_URL
            )
        else:
            # Send image to FastAPI backend
            with st.spinner("Analyzing your plant..."):

                # Prepare file for upload
                img_bytes = io.BytesIO()
                image.save(img_bytes, format="PNG")
                img_bytes.seek(0)

                files = {
                    "file": (
                        uploaded_file.name,
                        img_bytes,
                        "image/png"
                    )
                }

                try:
                    response = requests.post(
                        f"{API_URL}/predict",
                        files=files,
                        timeout=30
                    )

                    if response.status_code == 200:
                        data = response.json()

                        prediction = data["prediction"]
                        confidence = data["confidence"]

                        st.success(
                            f"Prediction: {prediction}"
                        )

                        st.info(
                            f"Confidence: {confidence}%"
                        )

                    else:
                        st.error(
                            "Prediction failed. "
                            f"Status code: {response.status_code}"
                        )

                except requests.exceptions.RequestException as e:
                    st.error(
                        f"Error connecting to backend: {e}"
                    )

else:
    st.info(
        "Please upload a plant leaf image to get started."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")
st.caption(
    "PlantCare AI • End-to-End Machine Learning Deployment"
)