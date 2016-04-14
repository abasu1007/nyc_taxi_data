import csv as csv 
from mpl_toolkits.basemap import Basemap
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd   

#Inline Plotting for Ipython Notebook 
%matplotlib inline 

test_file = open('./nyc_taxi_data.csv', 'r')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

df = DataFrame({'Lon':[], 'Lat':[]})

for row in test_file_object:
    try:
        df = df.append(DataFrame({'Lon':[float(row[5])], 'Lat':[float(row[6])]}), ignore_index = True)
        df = df.append(DataFrame({'Lon':[float(row[9])], 'Lat':[float(row[10])]}), ignore_index = True)
    
    except:
        continue

test_file.close()

pd.options.display.mpl_style = 'default' #Better Styling  
new_style = {'grid': False} #Remove grid  
matplotlib.rc('axes', **new_style)  
from matplotlib import rcParams  
rcParams['figure.figsize'] = (17.5, 17) #Size of figure  
rcParams['figure.dpi'] = 250

P=df.plot(kind='scatter', x='Lon', y='Lat',color='white',xlim=(-74.06,-73.77),ylim=(40.61, 40.91),s=.02,alpha=.6)

P.set_axis_bgcolor('black') #Background Color