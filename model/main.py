import pickle


class Main:

    def __init__(self):
        self.model_types = ['knn', 'rf', 'svm']
        self.models = [pickle.load(open(x+".p", "rb" ) ) for x in self.model_types]

    def predict(self, features):
        prediction_results = [x.predict(features) for x in self.models]
        return prediction_results