# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 21:06:48 2021

@author: mathe_smzt7in
"""

import matplotlib.pyplot as plt;
#variaveis como fig, gnt, receberão os parametros de subplots da biblioteca plt
fig, gnt = plt.subplots();
#no eixo y do gnt sera colocado valor de 0 a 50
gnt.set_ylim(0, 50);
#no eixo x do gnt sera colocado um valor de 0 a 160
gnt.set_xlim(0, 160);
#no eixo x do gnt sera colocado um label
gnt.set_xlabel('Dias de Projeto');
#no eixo y do gnt sera colocado um label
gnt.set_ylabel('Tarefas');
#no eixo y do gnt sera escolhido valores dentro de um array
gnt.set_yticks([15, 25, 35]);
#no eixo y do gnt sera colocado labels nos valores escolhidos
gnt.set_yticklabels(['Tarefa1','Tarefa2','Tarefa3']);
#sera mostrado a grid
gnt.grid(True);
'''
a barra sera quebrada nas posições no eixo x [(de 10 até 10+50),(de 100 até 100+20)
e (de 130 até 130+10)] e as posições que cobrira o eixo y sera (de 30 até 30+9) e
a cor da barra será vermelha
'''
gnt.broken_barh([(10,50), (100,20), (130,10)], (30,9), facecolors =('tab:red'));
'''
a barra sera quebrada nas posições do eixo x [(de 40 até 40+50)] e a posição
que cobrira o eixo y sera (de 20, até 20+9) e a cor da barra sera verde
'''
gnt.broken_barh([(40,50)], (20,9), facecolors =('tab:green'));
'''
a barra sera quebrada nas posições do eixo x [(de 110 até 110+10) e (de 150
até 150+10)] e a cobrirao eixo y (de 10 até 10+9) e a cor sera azul
'''
gnt.broken_barh([(110,10),(150,10)],(10,9), facecolors =('tab:blue'));
