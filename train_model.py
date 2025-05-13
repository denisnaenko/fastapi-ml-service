from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_and_save_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = RandomForestClassifier()
    clf.fit(X, y)

    os.makedirs("model", exist_ok=True)
    joblib.dump(clf, "model/model.joblib")

if __name__ == "__main__":
    train_and_save_model()
