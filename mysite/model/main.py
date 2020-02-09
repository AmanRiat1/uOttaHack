import pickle
from joblib import dump, load
import model
import numpy as np

class Main:

    def __init__(self):
        self.model_types = ['knn', 'rf', 'svm']
        self.models = model.all_models()

    def predict(self, features):
        prediction_results = [x.predict(features) for x in self.models]
        return max(prediction_results)*100


x = Main()
test= (np.array([1,18	,0	,0	,4	,4	,2	,2	,0	,0	,0	,0	,4	,3	,4	,3	,6]))
test = test.reshape(1,-1)
y = x.predict(test)
print (y)
