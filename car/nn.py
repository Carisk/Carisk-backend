import random
import datetime

import pickle 
import xgboost
from .extrapolation import Extrapolation

# from fastai import *
# from fastai.tabular.all import *
# import pandas as pd


class NeuralNetwork:
    """
    This class is used to predict accident risk
    """
    def __init__(self):
        self.model_name = 'xboost_model.sav' 
        self.encoder_name = 'label_encoder.sav'
        self.sex_label = {
            "Male": "Masculino",
            "Female": "Feminino"
        }
     
    def load_model(self):

        model = pickle.load(open('model/'+ self.model_name, "rb"))

        return model

    def load_encoder(self):

        encoder = pickle.load(open('model/'+ self.encoder_name, "rb"))

        return encoder

    def predict(self, data):

        encoder = self.load_encoder()

        model = self.load_model()

        extr = Extrapolation()

        weather, day_of_week, date, hour = extr.get_weather_data(data['latitude'], data['longitude'])

        if(data['sex'] == "Masculino" or data['sex'] == "Feminino"):
            victim_gender = [data['sex']] 
        else:
            victim_gender = self.sex_label[data['sex']]

        if day_of_week == 'SAB':
            day_of_week = 'SÁB'

        victim_gender = encoder['Victim gender'].transform([victim_gender])[0]
        weekday = encoder['Weekday'].transform([day_of_week])[0]
        weather = encoder['Weather'].transform([weather])[0]

        h, m = hour.split(':')
        time_of_day  = int(datetime.timedelta(hours=int(h),minutes=int(m)).total_seconds())

        # To do - time of year
        time_of_year = 0 

        # To do - predict
        # predictions = model.predict(data)
            
        return [{ 'title': 'Predict', 'result': 0.9 }]

# class RenatoFastAiANNModel:

#     def __init__(self):
#         pass

#     def predict(self, data):
#         if self.nn == None:
#             self.nn = load_learner('dataset/nn_params.fastai')
#         pred = self.nn.predict(self.preprocess_line(data))
#         ret = []
#         prs = pred[2]
#         i = 0
#         for cat in data_lm.vocab:
#             ret.push({
#                 'title': cat,
#                 'result': pred[2][i]
#             })
#         return ret
        
#     def preprocess_line(self, jsonf):
#         """
#         Recebe dict com dados de linha e tranforma em dataframe pandas
#         """
#         key_white_list = [
#             'Weekday', 'City', 'UF', 'Weather', 'Victim gender', # cat
#             'Latitude', 'Longitude', 'Veicule age', 'Victim age', 'Time of year', 'Time of day', # cont
#             'Accident cause' # y
#         ]
#         obj = {}
#         for k in jsonf.keys():
#             if k in key_white_list:
#             obj[k] = [jsonf[k]]

#         if 'Date' in jsonf.keys() and 'Time' in jsonf.keys():
#             obj['Time of year'] = [( datetime.datetime.strptime(jsonf['Date'] + ' ' + jsonf['Time'], '%d/%m/%Y %H:%M') - datetime.datetime.strptime(date.split('/')[2], '%Y') ).total_seconds()]
#         else:
#             obj['Time of year'] = [None]
        
#         if 'Time' in jsonf.keys():
#             obj['Time of day'] = [-datetime.datetime.strptime(time, '%H:%M').timestamp()]
#         else:
#             obj['Time of day'] = [None]
#         return pd.DataFrame(obj)
    
#     def train(self, path):
#         """
#         Realiza treinamento de rede neural
#         """
#         # Leitura do dataset
#         df = pd.read_csv("dataset/acidentes2020.csv", delimiter=';')

#         # Preprocessamento lat long
#         df['Latitude'] = df['Latitude'].map(lambda x: float(x.replace(',','.')))
#         df['Longitude'] = df['Longitude'].map(lambda x: float(x.replace(',','.')))

#         # Preprocessamento datas
#         ty = []
#         td = []
#         for i in range(len(df)):
#         date = df['Date'].loc[i]
#         time = df['Time'].loc[i]
#         acc_dt = datetime.datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M')
#         acc_ty = acc_dt - datetime.datetime.strptime(date.split('/')[2], '%Y')
#         acc_td = datetime.datetime.strptime(time, '%H:%M').timestamp()
#         acc_ty = acc_ty
#         ty.append(acc_ty.total_seconds())
#         td.append(-acc_td)
#         df['Time of year'] = ty
#         df['Time of day'] = td

#         # Carregamento dos dados
#         data_lm = TabularDataLoaders.from_df(
#             path='.',
#             df=df,
#             cat_names=['Weekday', 'City', 'UF', 'Weather', 'Victim gender'],
#             cont_names=['Latitude', 'Longitude', 'Veicule age', 'Victim age', 'Time of year', 'Time of day'],
#             procs=[FillMissing, Categorify, Normalize],
#             y_names='Accident cause',
#             valid_pct=0.2)

#         # Criação da rede neral
#         learn = tabular_learner(data_lm, metrics=[Precision(average='macro'), Recall(average='macro')])

#         # Treinamento da rede
#         learn.fit_one_cycle(7)
#         learn.fine_tune(1)
#         learn.fit_one_cycle(7)
#         learn.fine_tune(1)
#         learn.fit_one_cycle(7)
#         learn.fine_tune(1)
#         learn.fit_one_cycle(7)

#         self.nn = learn

#         self.nn.save('dataset/nn_params.fastai')


