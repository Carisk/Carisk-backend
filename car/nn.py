import random
import datetime

import pickle 
import xgboost
from fastai import *
from fastai.tabular.all import *
import pandas as pd


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

class RenatoFastAiANNModel:

    def __init__(self):
        pass

    def predict(self, data):
        if self.nn == None:
            self.nn = load_learner('dataset/nn_params.fastai')
        pred = self.nn.predict(self.preprocess_line(data))
        ret = []
        prs = pred[2]
        i = 0
        for cat in data_lm.vocab:
            ret.push({
                'title': cat,
                'result': pred[2][i]
            })
        return ret
        
    def preprocess_line(self, jsonf):
        """
        Recebe dict com dados de linha e tranforma em dataframe pandas
        """
        key_white_list = [
            'Weekday', 'City', 'UF', 'Weather', 'Victim gender', # cat
            'Latitude', 'Longitude', 'Veicule age', 'Victim age', 'Time of year', 'Time of day', # cont
            'Accident cause' # y
        ]
        obj = {}
        for k in jsonf.keys():
            if k in key_white_list:
            obj[k] = [jsonf[k]]

        if 'Date' in jsonf.keys() and 'Time' in jsonf.keys():
            obj['Time of year'] = [( datetime.datetime.strptime(jsonf['Date'] + ' ' + jsonf['Time'], '%d/%m/%Y %H:%M') - datetime.datetime.strptime(date.split('/')[2], '%Y') ).total_seconds()]
        else:
            obj['Time of year'] = [None]
        
        if 'Time' in jsonf.keys():
            obj['Time of day'] = [-datetime.datetime.strptime(time, '%H:%M').timestamp()]
        else:
            obj['Time of day'] = [None]
        return pd.DataFrame(obj)
    
    def train(self, path):
        """
        Realiza treinamento de rede neural
        """
        # Leitura do dataset
        df = pd.read_csv("dataset/acidentes2020.csv", delimiter=';')

        # Preprocessamento lat long
        df['Latitude'] = df['Latitude'].map(lambda x: float(x.replace(',','.')))
        df['Longitude'] = df['Longitude'].map(lambda x: float(x.replace(',','.')))

        # Preprocessamento datas
        ty = []
        td = []
        for i in range(len(df)):
        date = df['Date'].loc[i]
        time = df['Time'].loc[i]
        acc_dt = datetime.datetime.strptime(date + ' ' + time, '%d/%m/%Y %H:%M')
        acc_ty = acc_dt - datetime.datetime.strptime(date.split('/')[2], '%Y')
        acc_td = datetime.datetime.strptime(time, '%H:%M').timestamp()
        acc_ty = acc_ty
        ty.append(acc_ty.total_seconds())
        td.append(-acc_td)
        df['Time of year'] = ty
        df['Time of day'] = td

        # Carregamento dos dados
        data_lm = TabularDataLoaders.from_df(
            path='.',
            df=df,
            cat_names=['Weekday', 'City', 'UF', 'Weather', 'Victim gender'],
            cont_names=['Latitude', 'Longitude', 'Veicule age', 'Victim age', 'Time of year', 'Time of day'],
            procs=[FillMissing, Categorify, Normalize],
            y_names='Accident cause',
            valid_pct=0.2)

        # Criação da rede neral
        learn = tabular_learner(data_lm, metrics=[Precision(average='macro'), Recall(average='macro')])

        # Treinamento da rede
        learn.fit_one_cycle(7)
        learn.fine_tune(1)
        learn.fit_one_cycle(7)
        learn.fine_tune(1)
        learn.fit_one_cycle(7)
        learn.fine_tune(1)
        learn.fit_one_cycle(7)

        self.nn = learn

        self.nn.save('dataset/nn_params.fastai')


