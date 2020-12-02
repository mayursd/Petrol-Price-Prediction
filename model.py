import pandas as pd
df = pd.read_csv('C:/Users/mayur/Downloads/TrainData.csv')
df["Petrol (USD)"].fillna(df["Petrol (USD)"].mean(), inplace = True)
from sklearn.linear_model import LinearRegression
x = df[['Date']]
y = df[['Petrol (USD)']]
ln = LinearRegression()
ln.fit(x,y)
import pickle
f = open('Pricemodel.model','wb')
pickle.dump(ln,f)
f.close()
test = [2020]
model = pickle.load(open('Pricemodel.model','rb'))
prediction = model.predict([test])
print(prediction)
