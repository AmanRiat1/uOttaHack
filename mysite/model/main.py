import pickle
import numpy as np


class Main:

    def __init__(self):
        self.model_types = ['knn', 'rf', 'svm']
        self.models = [pickle.load(open('../trained_models/'+x+".sav", "rb" ) ) for x in self.model_types]

    def predict(self, features):
        prediction_results = [x.predict((np.array(features)).reshape(-1,1)) for x in self.models]
        return max(prediction_results)*100

p= Main()
y=p.predict([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2])
print(y)