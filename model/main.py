import pickle


class Main:

    def __init__(self):
        self.model_types = ['knn', 'rf', 'svm']
        self.models = [pickle.load(open(x+".p", "rb" ) ) for x in self.model_types]

    def predict(self, features):
        prediction_results = [x.predict(features) for x in self.models]
        return max(prediction_results)*100


    y = predict([1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2])