import pickle
from joblib import dump, load
from .model import all_models
import numpy as np

class Main:

    def __init__(self):
        self.model_types = ['knn', 'rf', 'svm']
        self.models = all_models()

    def predict(self, features):
        features = np.array(features)
        features = features.reshape(1,-1)
        prediction_results = [x.predict(features) for x in self.models]
        return (prediction_results[0])

