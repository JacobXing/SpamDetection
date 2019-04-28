# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 11:06:32 2018

@author: 13661
"""
import pandas as pd
import numpy as np
#from numpy import *
reader = pd.read_csv('../../../data_sets/honey_pot/preprocessed/dynamic_features_intermediate1.csv')
index = []
index = reader['user_id']
index = np.array(index)
index = index.astype(int)
index = index.astype(str)
reader2 = pd.read_csv("../../../data_sets/honey_pot/raw/all2.csv")
lastIndex=reader2.last_valid_index()
for i in range(len(index)):
    a = []
    for j in range(0,lastIndex):
        if index[i]==reader2.loc[j][0]:
            a.append(reader2.loc[j])
            dataframe = pd.DataFrame(a)
            dataframe.to_csv("../../../data_sets/honey_pot/preprocessed/Divided/test_{0}.csv".format(i), index=False,sep=',')
    print("finish iteration{0}".format(i))
'''
remove URL
'''
import re
for i in range(len(index)):
    f=pd.read_csv("../../../data_sets/honey_pot/preprocessed/Divided/test_{0}.csv".format(i))
    f['Tweet'] = f['Tweet'].apply(lambda x: re.split('http://[a-zA-Z0-9.?/&=:]*', str(x))[0])
    f.to_csv("../../../data_sets/honey_pot/preprocessed/Divided/test_{0}.csv".format(i), index=False,sep=',')

