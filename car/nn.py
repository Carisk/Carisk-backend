import pickle 
import xgboost

class NeuralNetwork:
    """
    This class is used to predict accident risk
    """
    def __init__(self):
    
        self.acidentes_label = [
            'Dangerous driving area',
            'Dangerous driving area',
            'Animals on the road',
            'People on the road',
            'Dangerous road',
            'Dangerous driving area',
            'Inattentive drivers',
            'Inattentive drivers']

    def load_pickle(filename):
        model = pickle.load(open('../model/'+ filename, "rb"))
        return model

    def predict(data):

        filename = 'xboost_model.sav'

        model = load_pickle(filename)

        predictions = model.predict(data)

        results = []

        for predict in predictions:
            results.append({ 'title': self.acidentes_label[pred], 'result': 0.1 })
            
        return results