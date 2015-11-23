import pandas as pd
import numpy as np

size = 5 # nu tut my blyat ukazyvaem razmer matricy

a = np.array(np.arange(size*size).reshape(size,size), dtype=float) #tut my generim ebannuyu matricu
for i in range(size):
    for j in range(size):
        if i>=size-j: a[i,j] = np.nan
            
a[0,3] = a[2,0] = np.nan # 2 znacheniya po kaifu zanulyaem


print('bylo ->\n',a) 

strok = []  #eto budut indexy strok epta
stolb = []  #eto stolbcov hule

for i in range(size): #generim ih ciklom dliny n, a ne n^2
    strok.extend([i]*(size-i))
    stolb.extend(range(size-i))
    
    
a[strok,stolb] = np.nan_to_num(a[strok,stolb]) #zaamenyaem tolko to chto po kaifu

print('\nstalo ->\n',a)
