import mlflow.sklearn

model = mlflow.sklearn.load_model("mlruns/154062067008891988/9eeda6cdf34c42feac8e204b9c00a9f7/artifacts/model")
vectorizer = mlflow.sklearn.load_model("mlruns/154062067008891988/9eeda6cdf34c42feac8e204b9c00a9f7/artifacts/vectorizer")

def predict_sentiment(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)
    return prediction[0]
