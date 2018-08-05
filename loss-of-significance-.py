# -*- coding: utf-8 -*-
"""
Created on Fri Aug 03 14:58:39 2018

@author: Benjamín Castro Pohl
"""
from numpy import math
from matplotlib import pyplot
import numpy as np

n = 4 #Cantidad de triángulos que parten circunferencia de radio 1

listarea = [] #Lista de las áreas desde la partición n hasta una partición de 2 triángulos
listaerror = [] #Lista de errores entre área n y área n-1
listaerror1 = [] #Lista de errores entre área n y área n-1
a = []
while n>2:
    theta = math.pi*2/n #Ángulo según partición
    area = n*(math.sin(theta/2)*math.cos(theta/2)) #Suma de las áreas de todos los triángulos    
    listarea.append(area)
    n-=1

la32 = np.asarray(listarea , dtype = np.float32) #La lista de áreas se convierte en un arreglo float32
la64 = np.asarray(listarea , dtype = np.float64) #La lista de áreas se convierte en un arreglo float64

for i in range(len(la32)-1):
    listaerror.append(-la32[i+1]+la32[i]) #Se agrega la diferencia de áreas consecutivas a una lista
for i in range(len(la64)-1):
    listaerror1.append(-la64[i+1]+la64[i]) #Se agrega la diferencia de áreas consecutivas a una lista

le32=np.asarray(listaerror , dtype = np.float32) #arreglo float32 de error entre áreai y áreai-1
le64=np.asarray(listaerror , dtype = np.float64) #arreglo float64 de error entre áreai y áreai-1

print la32[0]
print la64[0]
print le32[0]
print le64[0]
#Como las listas de áreas están ordenadas de más exactas a menos exactas (de mayor a menor) 
#se puede ver que en los arreglos de errores empieza a haber una tendencia a 0 a medida que el área
#se acerca a pi.