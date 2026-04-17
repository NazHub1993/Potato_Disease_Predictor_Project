# Potato Leaf Disease Predictor 🥔🌿

A full-stack Deep Learning application that classifies potato leaf diseases using a Convolutional Neural Network (CNN). The project features a React frontend, a FastAPI backend, and utilizes TensorFlow Serving via Docker for high-performance model inference.

## 🚀 Features
- **Real-time Prediction:** Upload an image of a potato leaf and get instant results.
- **Disease Categories:** Detects Early Blight, Late Blight, and Healthy leaves.
- **Scalable Inference:** Uses TensorFlow Serving to handle model versions efficiently.
- **Modern Tech Stack:** React, Tailwind CSS, FastAPI, TensorFlow, and Docker.

---

## 🛠 Project Architecture

The system is divided into three main components:
1. **Frontend:** React.js interface for image uploading and result visualization.
2. **Backend:** FastAPI server that handles image preprocessing and communicates with the model server.
3. **Model Server:** TensorFlow Serving running in a Docker container, hosting the trained CNN models.



---

## 📂 Model Versioning
I have experimented with 4 different model iterations. 
- **Current Version:** `4` (Most Accurate)
- **Status:** Version 4 has been optimized for the highest accuracy and lowest false-negative rate, especially for the "Healthy" class.

---

## 🏃‍♂️ Getting Started

### 1. Model Server (TensorFlow Serving with Docker)
The models are served using a Docker container. Make sure you have Docker Desktop running.

Run the following command from the project root to start serving **Version 4**:

```bash
docker run -t --rm -p 8501:8501 \
    --name potato_tfs \
    -v "F:/.../models:/models" \
    -e MODEL_NAME=plant_model \
    tensorflow/serving


Start the server:

Bash
python -m uvicorn app.main:app --reload


Start the frontend:
npm run dev
```  <-- These three dots "close" the bash section

## 📸 Screenshots
Here is a look at the Potato Disease Predictor in action:
<img width="1279" height="855" alt="image" src="https://github.com/user-attachments/assets/cab1893c-f103-4712-83f7-1d29652bf8de" />

localhost:8501 showing that model 4 is running:
<img width="393" height="447" alt="image" src="https://github.com/user-attachments/assets/1c990f5d-f8ae-4c5c-b5e2-a0f79a245d87" />

Server running on localhost 8000:
<img width="454" height="200" alt="image" src="https://github.com/user-attachments/assets/c3ccf3cf-d093-4d3c-867f-89d2d0517638" />






