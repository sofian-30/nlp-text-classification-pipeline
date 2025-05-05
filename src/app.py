
from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_sentiment

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input: TextInput):
    sentiment = predict_sentiment(input.text)
    return {"prediction": sentiment}
