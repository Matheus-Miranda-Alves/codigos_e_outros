# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:13:16 2021

@author: mathe_smzt7in
"""

import matplotlib.pyplot as plt;
#1 Lista de Rotulos, que são labels
labels='Sem instrução e menos de 1 ano de estudo','Ensino fundamental incompleto ou equivalente','Ensino fundamental completo ou equivalente','Ensino médio incompleto ou equivalente','Ensino médio completo ou equivalente','Ensino superior incompleto ou equivalente','Ensino superior completo ou equivalente','Não determinado';
#Um arrey com as sizes(tamanhos)
sizes=[15394,70634,15258,13267,48376,8973,25286,0];
#Um Array de Cores
colors=['gold','yellowgreen','coral','lightskyblue','red','grey','cyan','blue'];
'''
pegara(patchs)a lista de setores dos gráficos, (texts) a lista de
textos que serão usados como labels e (autotexts) os valores de 
cada setor, e serão modificados por pie
O metodo pie, que pegara as variaveis e utilizara de parametros
automaticamente pegara os valores e transforamara em porcentagem, sem
ponto flutuante(%1.0f%%), e que o angulo indicado sera de de 90 graus no sentido anti-horario(startangle=90)'''
patches, texts,autotexts = plt.pie(sizes, colors=colors, autopct='%1.0f%%', startangle=90);
#Metodo legend transformara as informações em legendas
plt.legend(patches, labels, loc="lower right")
plt.axis('equal');
plt.show();