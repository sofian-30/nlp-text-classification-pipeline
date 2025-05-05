
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def load_and_preprocess(filepath):
    data = pd.read_csv(filepath)
    X_train, X_test, y_train, y_test = train_test_split(
        data['text'], data['label'], test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    return X_train_vec, X_test_vec, y_train, y_test, vectorizer
