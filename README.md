# 🌱 PlantCare AI — Plant Disease Detection

An end-to-end machine learning application that detects **38 types of plant diseases** from leaf images using a Convolutional Neural Network (MobileNetV2 with transfer learning).

Built as a **Capstone Project** demonstrating the full ML deployment pipeline: model training → serialization → REST API → frontend UI → Docker containerization → cloud hosting.

---

## Project Structure

```
plant-disease-capstone/
│
├── model/
│   ├── plant_disease_model.keras    # Trained Keras model (MobileNetV2)
│   └── class_names.json             # 38 disease class labels
│
├── app/
│   ├── main.py                      # FastAPI backend (REST API)
│   └── index.html                   # Lightweight HTML frontend
│
├── streamlit_app.py                 # Streamlit dashboard (connects to API)
├── train.py                         # Model training script
├── Dockerfile                       # Docker container configuration
├── requirements.txt                 # Python dependencies
├── .gitignore
└── .dockerignore
```

---

## Supported Plant Diseases

The model can classify **38 classes** across 14 plant species, including:

| Plant | Diseases |
|-------|----------|
| Apple | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| Tomato | Bacterial Spot, Early/Late Blight, Leaf Mold, Septoria, Target Spot, Mosaic Virus, Yellow Leaf Curl, Healthy |
| Corn | Cercospora Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| Grape | Black Rot, Esca, Leaf Blight, Healthy |
| Potato | Early Blight, Late Blight, Healthy |
| And more... | Pepper, Cherry, Peach, Orange, Strawberry, etc. |

---

## How to Run Locally

### Prerequisites

- Python 3.11+
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/Rithikbalan12/plant-disease-capstone.git
cd plant-disease-capstone
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI Backend

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: `http://127.0.0.1:8000`

### 4. Start the Streamlit Frontend (Optional)

Open a new terminal and run:

```bash
streamlit run streamlit_app.py
```

The dashboard will open at: `http://localhost:8501`

---

## API Endpoints

### `GET /health` — Health Check

```bash
curl http://127.0.0.1:8000/health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "PlantCare AI API is running"
}
```

### `POST /predict` — Disease Prediction

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -F "file=@leaf_image.jpg"
```

**Response:**
```json
{
  "prediction": "Tomato___Late_blight",
  "confidence": 97.85
}
```

### `GET /` — Web Interface

Open `http://127.0.0.1:8000` in a browser to use the built-in HTML frontend.

---

## Testing with Postman

1. Open Postman and create a new **POST** request.
2. Set the URL to: `http://127.0.0.1:8000/predict`
3. Go to the **Body** tab → select **form-data**.
4. Add a key named `file`, set the type to **File**, and upload a leaf image.
5. Click **Send** to get the prediction.

---

## Docker Deployment

### Build the Docker Image

```bash
docker build -t plantcare-ai .
```

### Run the Container

```bash
docker run -p 8000:8000 plantcare-ai
```

The API will be live at `http://localhost:8000`.

---

## Cloud Deployment (Render)

1. Push the repository to GitHub.
2. Go to [Render](https://render.com) and create a new **Web Service**.
3. Connect your GitHub repository.
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`
5. Deploy and get your public URL.

---

## Model Details

| Property | Value |
|----------|-------|
| Architecture | MobileNetV2 (Transfer Learning) |
| Input Size | 224 × 224 × 3 (RGB) |
| Framework | TensorFlow / Keras |
| Dataset | PlantVillage (38 classes) |
| Training | 10 epochs, Adam optimizer, Early Stopping |
| Preprocessing | Resize to 224×224, normalize pixel values to [0, 1] |

---

## Tech Stack

| Component | Technology |
|-----------|------------|
| Backend API | FastAPI + Uvicorn |
| Frontend | Streamlit, HTML/CSS/JS |
| ML Framework | TensorFlow / Keras |
| Model | MobileNetV2 (pretrained on ImageNet) |
| Containerization | Docker |
| Cloud Hosting | Render / Railway / AWS |

---

## Author

**Rithik Balan**

Capstone Project — End-to-End AI Project Deployment
