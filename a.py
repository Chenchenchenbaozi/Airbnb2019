import numpy as np
import pandas as pd
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import os
os.environ["PROJ_LIB"] = r"C:\Users\Qianyu\Anaconda3\Library\share";
from mpl_toolkits.basemap import Basemap
import matplotlib.colors as mcolors


db = pd.read_csv(r'C:\Users\Qianyu\Desktop\airbnb.csv', engine='python')
print(db.columns.values)
list1 = [1]*100
db.dropna(subset=['zipcode'], inplace=True)
db.dropna(subset=['price'], inplace=True)
print(len(db['review_scores_rating']))
dict = {}

zip1 = db['zipcode'].tolist()
prices = db['price'].tolist()
for indexs in db.index:

    key = str(zip1[indexs])
    price = float(prices[indexs].replace('$','').replace(',',''))
    if key not in dict.keys():
        dict[str(key)] = price
    else:

        dict[str(key)] += price
        #print(list(dict.keys()))
        a = list(dict.keys()).index(key)
        list1[a] += 1
#print(dict,list1)
l = len(dict)
list_new = list1[:l]
values = list(dict.values())
new_zip = list(dict.keys())
avg_price =list(np.round(np.array(values)/np.array(list_new),2))
new_dict = {k: v for k, v in zip(new_zip, avg_price)}
print(len(new_dict))
code = '80331,80333,80335,80336,80337,80339,80469,80538,80539,80634,80636,80637,80638,80639,80686,80687,80689,80796,80797,80798,80799,80801,80802,80803,	80804,80805,80807,80809,80933,80935,80937,80939,80992,80993,80995,80997,	80999,81241,81243,81245,81247,	81249,81369,81371,81373,81375,81377,81379,81475,81476,81477,81479,81539,81541,	81543,81545,81547,81549,81667,81669,81671,81673,81675,81677,81679,81735,	81737,81739,	81825,81827,	81829,	81925,81927,	81929'
zip_list = [s for s in code.split(',')]
for key in list(new_dict.keys()):
    if key not in zip_list:
        del new_dict[key]
print(len(new_dict))
max1 = max(new_dict.values())
print([k for k,v in new_dict.items() if v == max1])

fig     = plt.figure()
ax      = fig.add_subplot(111)
m=Basemap(projection='cyl',llcrnrlat=48.05, urcrnrlat=48.25, llcrnrlon=11.76, urcrnrlon=11.31,resolution='h')
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='w',lake_color='aqua')
m.drawcoastlines()
m.readshapefile(r'C:\Users\Qianyu\Downloads\plz-gebiete\plz-gebiete', 'area')



colvals = new_dict.values()
cdict = {'red':  ((0.0, 0.0, 0.0),
                 (1/6., 0.0, 0.0),
                 (1/2., 0.8, 1.0),
                 (5/6., 1.0, 1.0),
                 (1.0, 0.4, 1.0)),

             'green':  ((0.0, 0.0, 0.4),
                 (1/6., 1.0, 1.0),
                 (1/2., 1.0, 0.8),
                 (5/6., 0.0, 0.0),
                 (1.0, 0.0, 0.0)),

             'blue': ((0.0, 0.0, 0.0),
                 (1/6., 0.0, 0.0),
                 (1/2., 0.9, 0.9),
                 (5/6., 0.0, 0.0),
                 (1.0, 0.0, 0.0))

        }



cmap = mcolors.LinearSegmentedColormap(
'my_colormap', cdict, 100)
#cmap=plt.cm.GnYlRr#
cmap = mcolors.LinearSegmentedColormap.from_list("", ["green","yellow","red"])
norm=plt.Normalize(min(colvals),max(colvals))

patches   = []


for info, shape in zip(m.area_info, m.area):
    if info['plz'] in list(new_dict.keys()):
        color=cmap(norm(new_dict[info['plz']]))
        patches.append( Polygon(np.array(shape), True, color=color) )
pc = PatchCollection(patches, match_original=True, edgecolor='k', linewidths=1., zorder=2)
ax.add_collection(pc)

#colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array(colvals)
fig.colorbar(sm, ax=ax)

plt.show()