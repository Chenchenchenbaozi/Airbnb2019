import pandas as pd

db = pd.read_csv(r'C:\Users\Qianyu\Desktop\airbnb.csv', engine='python')
print(db.columns.values)
db = db.drop(['Unnamed: 0', 'neighborhood_overview', 'description','property_type', 'amenities'], axis=1)
print(db.columns.values)
cols = ['price', 'cleaning_fee', 'extra_people']
for col in cols:
    db[col] = db[col].map(lambda x: str(x).lstrip('$'))
print(len(db.index))
db.dropna()
print(len(db.index))
code = '80331,80333,80335,80336,80337,80339,80469,80538,80539,80634,80636,80637,80638,80639,80686,80687,80689,80796,80797,80798,80799,80801,80802,80803,	80804,80805,80807,80809,80933,80935,80937,80939,80992,80993,80995,80997,	80999,81241,81243,81245,81247,	81249,81369,81371,81373,81375,81377,81379,81475,81476,81477,81479,81539,81541,	81543,81545,81547,81549,81667,81669,81671,81673,81675,81677,81679,81735,	81737,81739,	81825,81827,	81829,	81925,81927,	81929'
zip_list = [s for s in code.split(',')]

db = db[db['zipcode'].isin(zip_list)]
print(len(db.index))
db.to_csv(r'C:\Users\Qianyu\Desktop\new_airbnb.csv')
