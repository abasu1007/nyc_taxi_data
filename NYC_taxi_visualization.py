# csv and numpy packages are imported

import csv as csv 
from mpl_toolkits.basemap import Basemap
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Open up the csv file in to a Python object
csv_file_object = csv.reader(open('./nyc_taxi_data.csv')) 
header = csv_file_object.next()  

test_file = open('./nyc_taxi_data.csv', 'r')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

my_map = Basemap(projection='merc', lat_0=40.7128, lon_0=-74.0059,
    resolution = 'h', area_thresh = 0.001,
    llcrnrlon=-74.018629, llcrnrlat=40.704889,
    urcrnrlon=-73.905500, urcrnrlat=40.831201)
 
my_map.drawcoastlines()
my_map.drawcountries()
my_map.drawrivers()
my_map.fillcontinents(color='coral',lake_color='aqua')
my_map.drawmapboundary(fill_color='aqua')

my_map.drawmeridians(np.arange(0, 360, 30))
my_map.drawparallels(np.arange(-90, 90, 30))

pickup_df = DataFrame({'Lon':[], 'Lat':[]})
dropoff_df = DataFrame({'Lon':[], 'Lat':[]})


for i in range (5000):
    row = test_file_object.next()
    pickup_df = pickup_df.append(DataFrame({'Lon':[float(row[5])], 'Lat':[float(row[6])]}), ignore_index = True)
    dropoff_df = dropoff_df.append(DataFrame({'Lon':[float(row[9])], 'Lat':[float(row[10])]}), ignore_index = True)

test_file.close()


for row in range (len(pickup_df)):
    x1,y1 = my_map(pickup_df['Lon'][row], pickup_df['Lat'][row])
    x2,y2 = my_map(dropoff_df['Lon'][row], dropoff_df['Lat'][row])

    my_map.plot(x1, y1, 'bx', markersize=5)
    my_map.plot(x2, y2, 'ro', markersize=5)
    
plt.show()

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