# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 22:16:39 2021

@author: mathe_smzt7in
"""

from pandas import read_csv
from matplotlib import pyplot
series = read_csv(r"C:\Users\mathe_smzt7in\USD_BRL_hist.csv",header=0,index_col=0,parse_dates=True, squeeze=True);
series.plot();
pyplot.show;