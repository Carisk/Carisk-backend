import random
from operator import itemgetter

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .extrapolation import Extrapolation
from .nn import NeuralNetwork

# Create your views here.
class CarView(APIView):
    """
    This is the predicion view.
    It has a single endpoint called POST '/predict/'
    When a message is sent to it, it's parsed and a 
    prediction is generated, parsed and returned to user
    """

    def post(self, request, *args, **kwargs):
        data_extrapolation = Extrapolation()
        neural_network = NeuralNetwork()

        # Collect basic data
        data = {
            'latitude':     request.data['latitude'],
            'longitude':    request.data['longitude'],
            'sex':          request.data['sex'],
            'vehicle_type': request.data['vehicle_type'],
            'vehicle_age':  validate_integer(request.data['vehicle_age']),
            'age':          validate_integer(request.data['age']),
        }

        # Extrapolate remaining data
        data['climate'] = data_extrapolation.get_climate(
            request.data['latitude'],
            request.data['longitude']
        )

        # Predict
        predictions = NeuralNetwork.predict(data)

        # Parse prediction
        predictions = sorted(predictions, key=itemgetter('result'), reverse=True)
        most_likely = predictions[0]['title']

        # Represents it correctly for frontend use
        response = manage_predictions(predictions)

        # Response
        response['most_likely'] = most_likely
        response['nn_input'] = data
        return Response(response, status=status.HTTP_200_OK)

def validate_integer(supposed_integer):
    try:
        integer = int(supposed_integer)
    except:
        return None
    return integer    

def manage_predictions(predictions):
    # Urls of signs used
    urls_sign = {
        'Animals on the road':          'https://github.com/Carisk/Carisk-backend/blob/feature/manage-prediction/images/animals_on_road.png',
        'People on the road':           'https://github.com/Carisk/Carisk-backend/blob/feature/manage-prediction/images/people_on_road.png',
        'Dangerous driving area':       'https://imagepng.org/wp-content/uploads/2018/08/alerta.png',
        'Dangerous road':               'https://isinaliza.vteximg.com.br/arquivos/ids/169750-1000-1000/3597-placa-pista-escorregadia-a-28-aluminio-refletivo-acm-100x100cm-1.jpg?v=636800685747170000',
        'Inattentive drivers':          'https://imagepng.org/wp-content/uploads/2018/08/alerta.png',
        'Dangerous drivers':            'https://imagepng.org/wp-content/uploads/2018/08/alerta.png',
        'Dangerous climate conditions': 'https://imagepng.org/wp-content/uploads/2018/08/alerta.png'
    }
    default_sign_url = 'https://imagepng.org/wp-content/uploads/2017/08/placa-de-pare.png'
    
    # Choosing best prediction
    best_prediction = predictions[0]
    for pred in predictions:
        if pred['result'] > best_prediction['result']:
            best_prediction['result'] = pred['result']
    
    # Generating response
    if best_prediction['result'] >= 0.3:
        if best_prediction['result'] < 0.7:
            background_color = '#F4ECCF'
        else:
            background_color = '#F4CFCF'
        show_sign = True
        show_spinner = False
        primary_text = best_prediction['title']
        sign_url = urls_sign.get(best_prediction['title'], default_sign_url)
        secondary_text = 'Pay atention, the worst risk is ' + best_prediction['title']
    else:
        background_color = '#E3EFF5'
        show_sign = False
        show_spinner = True
        sign_url = default_sign_url
        primary_text = 'No predictions'
        secondary_text = 'There are few risks, but be careful yet'

    response = {
        'backgroundColor':  background_color,
        'showSign' :        show_sign,
        'showSpinner' :     show_spinner,
        'signUrl' :         sign_url,
        'primaryText' :     primary_text,
        'secondaryText' :   secondary_text,
        'most_likely' :     '',
        'nn_input' :        '',
    }

    return response