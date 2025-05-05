# 🧠 NLP Text Classification Pipeline 🚀

This project provides a complete **NLP text classification pipeline** using supervised machine learning techniques. It includes **training, experiment tracking with MLflow**, an **API using FastAPI** for real-time predictions, and a **CI/CD pipeline via GitHub Actions**.

---

## 🔍 Project Goal

The goal is to automatically predict the **sentiment** (positive or negative) of a given text review. The pipeline combines:

- **Text vectorization** (TF-IDF)
- **Supervised model** (Logistic Regression)
- **Experiment tracking with MLflow**
- **API deployment via FastAPI**
- **Unit tests with pytest**
- **CI/CD automation via GitHub Actions**

---

## 🧰 Tech Stack

- `Python 3.10` – core language  
- `pandas` – data handling  
- `scikit-learn` – model training and TF-IDF vectorization  
- `MLflow` – experiment and model tracking  
- `FastAPI` – REST API  
- `Uvicorn` – ASGI server  
- `pytest` – unit testing  
- `GitHub Actions` – continuous integration (CI/CD)
- `Docker & Docker Compose` – containerization and orchestration

---

## 📁 Project Structure

```
nlp_text_classification_pipeline/
├── data/
│   └── raw/sample_reviews_200.csv
├── src/
│   ├── app.py                # FastAPI app
│   ├── data_preprocessing.py
│   ├── model_training.py     # MLflow logging
│   └── predict.py            # Load model and predict
├── tests/
│   ├── test_predict.py       # Unit tests
│   └── test_api.py
├── .github/
│   └── workflows/ci-cd.yml   # CI pipeline
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/nlp_text_classification_pipeline.git
cd nlp_text_classification_pipeline
```

2. **Create virtual environment**  
```bash
python -m venv .venv
source .venv/bin/activate        # Linux/Mac
.venv\Scripts\activate         # Windows
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

---

## 🏋️‍♂️ Train the Model

```bash
python -m src.model_training
```

This will:
- Preprocess and vectorize the text data
- Train a logistic regression classifier
- Automatically log the model, vectorizer, and metrics to **MLflow**

To launch the MLflow tracking UI:
```bash
mlflow ui
```
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚀 Run the FastAPI Server

```bash
uvicorn src.app:app --reload
```

Open the interactive API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Run Tests

```bash
pytest
```

You can also test a live prediction via curl:
```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d "{\"text\": \"I love this movie!\"}"
```

---

## 🐳 Docker & Docker Compose

To run the project using Docker:

1. **Build and start containers**
```bash
docker-compose up --build
```

2. **Access the services:**
- FastAPI: [http://localhost:8000/docs](http://localhost:8000/docs)
- MLflow: [http://localhost:5000](http://localhost:5000)

Example `docker-compose.yml`:
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    command: uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload

  mlflow:
    image: ghcr.io/mlflow/mlflow
    ports:
      - "5000:5000"
    environment:
      - MLFLOW_TRACKING_URI=http://mlflow:5000
    command: mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root /mlruns
    volumes:
      - ./mlruns:/mlruns
```

---

## 🔄 CI/CD with GitHub Actions

The project uses GitHub Actions to:

- ✅ Install dependencies  
- ✅ Run unit tests  
- ✅ Trigger on push or pull request to the `main` branch  

See the workflow file at `.github/workflows/ci-cd.yml`.

---

## 🌱 Future Enhancements

- Integrate a lightweight **LLM** from Hugging Face (e.g. `distilbert-base-uncased`)
- Add more advanced preprocessing (lemmatization, emoji/text cleaning)
- Deploy API via **Docker**, **Render**, or **Railway**

---

## 👨‍💻 Author

**Sofian OUASS**  
Big Data Engineer & Data Scientist  
📍 Montpellier, France  
🔗 [GitHub Profile](github.com/sofian-30)
