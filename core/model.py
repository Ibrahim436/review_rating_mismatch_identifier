import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import keras 
from keras.models import load_model
import pandas as pd
import numpy as np
import os

class Predict():
    def __init__(self, ):
        self.model = load_model('bert_model_v1.h5',
                      custom_objects={'KerasLayer':hub.KerasLayer})

    
    def predict(self,input):
        df=pd.read_csv(input)
        result=self.model.predict(df['Text']).flatten()
        result=np.where(result>0.5,1,0)
        df['preds']=result
        df['actual']=df['Star'].apply(lambda x:1 if x>3 else 0)
        non_match=df[df.preds != df.actual]
        if non_match.shape[0]>0:
            non_match['Developer Reply']='Text semantics not matching with rating'
        return non_match[['ID','Text','Star','User Name','Developer Reply']]


