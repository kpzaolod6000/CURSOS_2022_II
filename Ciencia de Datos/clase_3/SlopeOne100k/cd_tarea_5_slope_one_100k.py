# -*- coding: utf-8 -*-
"""CD_tarea_5_SLopeOne100k

Automatically generated by Colaboratory.


## Importando librerias
"""
import pandas as pd
import numpy as np
from time import time
from secretstorage import Item
from Matrizdev import matrixDev
from Predict import getPredict
from indexMatrix import indexMatrix
from desEstandar import desStandard

from columnsName import getColumnsName

"""## Leendo el data

"""


data_ratings = pd.read_csv(r"/home/judal/Documentos/CURSOS_2022_II/Ciencia de Datos/clase_3/SimCosenoAJus100k/ratings.dat",sep=",", header=None, names=['userId','movieId','rating','times'])
df_Data = data_ratings.pivot_table(index='userId', columns='movieId', values='rating')
print("Dataset\n")
print(df_Data)


columns_names = getColumnsName(df_Data)
# print(columns_names)

"""## Algoritmo de Slope One

# ### Desviación Estandar
# """
print("Para hallar el Slope One ingrese los siguientes valores\n")
item1 = int(input("Item 1: "))
item2 = int(input("Item 2: "))

item_1 = df_Data[item1].to_numpy()
item_2 = df_Data[item2].to_numpy()

desv,card = desStandard(item_1,item_2)

print("\n\nEl Slope One (desviacion) del item ",item1," e item ",item2 , " es: ",desv)
print("\n\n")


"""### Construccion de la matriz"""
n_tam = len(columns_names)

start_time = time()
np_Matrix,cardinls = indexMatrix(n_tam,df_Data.to_numpy())
# print(np_Matrix)

Matrixdev,cardinls = matrixDev(np_Matrix,cardinls,columns_names)
elapsed_time = time() - start_time
print("Tiempo transcurrido: %0.10f segundos." % elapsed_time )

print("\nMatriz de desviacion estandar\n")
print(Matrixdev)
# print(cardinls)

# """### Predicción"""

print("\n")
user_predict =  int(input("Escriba el usuario calificador: "))
item_cal =  int(input("Escriba el item a calificar: "))

predict = getPredict(df_Data,Matrixdev,cardinls,user_predict,item_cal,columns_names)
print("\n")
print("EL usuario con id: ",user_predict," podria calificar a la pelicula con id de: ",item_cal, " con un puntaje de: " ,predict)


# print("lista de la fila: ", user_predict)
# test_ = df_Data.loc[user_predict,:].dropna().to_numpy()
# print(test_)
# print(np.count_nonzero(test_ == 1.0))
# print(np.count_nonzero(test_ == 2.0))
# print(np.count_nonzero(test_ == 3.0))
# print(np.count_nonzero(test_ == 4.0))
# print(np.count_nonzero(test_ == 5.0))