
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error,mean_absolute_error

import numpy as np
import pandas as pd

df = pd.read_csv(r"C:\Users\Ардак\Documents\Python machine learning\UNZIP_ME_FOR_NOTEBOOKS_ML_RUS_V6\DATA\new.csv")
df['SalePrice'] = df['SalePrice']//100
df = df.drop('Unnamed: 0', axis=1)




def model():
    X = df.drop('SalePrice', axis=1)
    y = df["SalePrice"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)
    model = LinearRegression()
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    MAE = mean_absolute_error(y_test, y_pred)
    MSE = mean_squared_error(y_test, y_pred)
    RMSE = np.sqrt(MSE)

    #print(df.iloc[[1]].drop('SalePrice',axis=1))
    print(model.predict(df.iloc[[1]].drop('SalePrice',axis=1))//1000*3.5)


print(df.tail())