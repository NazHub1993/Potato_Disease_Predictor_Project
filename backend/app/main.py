from fastapi import FastAPI, File, UploadFile
import requests
import numpy as np
from PIL import Image
import io

from .config import TF_SERVING_URL, CLASS_NAMES
from .utils import preprocess_image
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")

        processed_image = preprocess_image(image)

        payload = {
            "instances": [processed_image]
        }

        response = requests.post(TF_SERVING_URL, json=payload)

        if response.status_code != 200:
            return {"error": response.text}

        predictions = response.json()["predictions"][0]

        predicted_class = CLASS_NAMES[np.argmax(predictions)]
        confidence = float(np.max(predictions))

        return {
            "class": predicted_class,
            "confidence": confidence
        }
    
        

    except Exception as e:
        return {"error": str(e)}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
