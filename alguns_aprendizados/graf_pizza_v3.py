# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 20:25:31 2021

@author: mathe_smzt7in
"""

import matplotlib.pyplot as plt;
#1 Lista de Rotulos, que são labels
labels='Nenhum', 'Fundamental', 'Médio', 'Superior';
#Um arrey com as sizes(tamanhos)
sizes=[86026,28525,57394,25286];
#Um Array de Cores
colors=['lightgray','orange','coral','red'];
'''
pegara(patchs)a lista de setores dos gráficos, (texts) a lista de
textos que serão usados como labels e (autotexts) os valores de 
cada setor, e serão modificados por pie
O metodo pie, que pegara as variaveis e utilizara de parametros
automaticamente pegara os valores e transforamara em porcentagem, 
com um ponto flutuante(%1.1f%%), e que o angulo indicado sera de 
90 graus no sentido anti-horario(startangle=90)
'''
patches, texts,autotexts = plt.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90);
#Metodo legend transformara as informações em legendas
plt.legend(patches, labels, loc="lower right");
plt.axis('equal');
plt.show();