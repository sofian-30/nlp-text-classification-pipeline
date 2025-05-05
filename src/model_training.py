
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from src.data_preprocessing import load_and_preprocess

def train_model():
    mlflow.set_experiment("NLP_Text_Classification")

    with mlflow.start_run():
        X_train, X_test, y_train, y_test, vectorizer = load_and_preprocess("data/raw/sample_reviews_200.csv")

        model = LogisticRegression()
        model.fit(X_train, y_train)
        
        accuracy = model.score(X_test, y_test)

        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "model")
        mlflow.sklearn.log_model(vectorizer, "vectorizer")

        print(f"Model trained and logged with accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    train_model()
