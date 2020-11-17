from extrapolation import Extrapolation

class NeuralNetwork():
    """
    This class is used to predict accident risk
    """
    def load_pickle(path):
        pass

    def predict(data):
        
        extrapolation = Extrapolation()
        weather = extrapolation.get_climate(-23.46052014,-46.48772478)
        day_of_week = extrapolation.get_day_of_week(-23.46052014,-46.48772478)
        date = extrapolation.get_date(-23.46052014,-46.48772478)
        time_timezone = extrapolation.get_time_from_timezone(-23.46052014,-46.48772478)
        city = extrapolation.get_city(-23.46052014,-46.48772478)
        
        return [
           # { 'title': 'morte subita por queda de avião monomotor', 'result': 0.1 },
           # { 'title': 'atirador de elite',                         'result': 0.5 },
           # { 'title': 'explosão',                                  'result': 0.3 },
           # { 'title': 'alienigenas',                               'result': 0.9 },
           weather,
           city,
           day_of_week,
           date,
           time_timezone
        ]
    
nn = NeuralNetwork()
x = nn.predict()    
print(x)