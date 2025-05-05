
from src.predict import predict_sentiment

def test_predict_positive():
    assert predict_sentiment("I loved this movie!") == "positive"

def test_predict_negative():
    assert predict_sentiment("It was a terrible experience.") == "negative"
