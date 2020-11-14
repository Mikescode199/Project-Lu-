#//////////// LIBRERIAS DE IA ////////////
import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras import layers 
# ////////////////////
import pandas as pd 

#///////// Comienza a trabajar LU /////////
df = pd.read_csv('administrador_datosusuario.csv')
#DATASET
dataset = df.values
edad_x = dataset[:,2:3]
graduacion_ojo_derecho_y = dataset[:,1:2]

#MODELO 
def build_model():
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[2]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001)

    model.compile(loss='mse',
    optimizer=optimizer,
    metrics=['mae','mse'])

    return model

model = build_model()
model.fit(edad_x, graduacion_ojo_derecho_y,verbose=1)

