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
        response = {}
        response['backgroundColor'] = '#aadada'
        response['showSign'] = False
        response['showSpinner'] = False
        response['signUrl'] = ''
        response['primaryText'] = most_likely
        response['secondaryText'] = 'Be careful! Be paranoid! Imminent death risk!!!'

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