from .functions import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error,mean_absolute_error

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv(r"C:\Users\Ардак\Documents\Python machine learning\UNZIP_ME_FOR_NOTEBOOKS_ML_RUS_V6\DATA\new.csv")
df['SalePrice'] = df['SalePrice']//100
df = df.drop('Unnamed: 0', axis=1)

arr = []

def filter_money():

    min_ = int(input('Мин Сумма Денег:  '))
    max_ = int(input('Макс Сумма Денег:  '))
    min_room = int(input('Мин Сумма Комнат: '))
    dm = df[(df['SalePrice'] > min_) & (df['SalePrice'] < max_) & (df['TotRms AbvGrd'] > min_room)]
    print(dm.head(50)[['Lot Area', 'Year Built','TotRms AbvGrd', 'SalePrice']])
    print("Корзина : \n"
          "1.Добавить  \n"
          "2.Выйти \n")
    word = int(input("Выбрать: "))
    if word == 1:
        n = int(input('Напишите номер товара: '))
        arr.append(n)
        print("Товар добавлен в корзину *  \n")




def change():
    print('Выберите действие : \n'
          '1.Посмотреть средную цену для квартир с похожими параметрами \n'
          '2.Посмотреть график с ценами квартир \n'
          '3.Посмотреть рекомендованную цену для выложенной квартиры \n'
          '4.Выход \n')
    choice = int(input('Выберите категорию: '))

    while True:
        if choice==1:
            print(df[(df['SalePrice'] > 1600) & (df['SalePrice'] < 2100) & (df['TotRms AbvGrd'] > 7)][['Lot Area', 'TotRms AbvGrd', 'SalePrice']].head(30))
            change()
            break
        elif choice==2:
            sns.displot(data=df, x='SalePrice', height=6, aspect=2, bins=80, kde=True)
            plt.show()
            change()
            break
        elif choice==3:
            print('Лучшая цена для вашего дома по нашим меркам :  \n')
            model()
            print("Спасибо , что воспользовались нашей услугой! \n")
            break
        elif choice==4:
            print("Вы вышли в главное меню \n")
            break



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
    print(model.predict(df.iloc[[1]].drop('SalePrice',axis=1))//1000*3.5);





def change_info():
    print("Ваши данные :  \n")
    print(df.tail(1))
    print('Выберите Категорию : \n'
          '1.Изменить цену \n'
          '2.Выйти \n')
    choice = int(input('Выберите :'))
    n=0
    if choice==1:
        n = int(input("Вводите желаемую цену:  "))
        df.at[2924,"SalePrice"]=n
        print(df.tail())
        print('Данные успешно изменены! \n')




