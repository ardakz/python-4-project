
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Ардак\Documents\Python machine learning\UNZIP_ME_FOR_NOTEBOOKS_ML_RUS_V6\DATA\new.csv")
df['SalePrice'] = df['SalePrice']//100
df = df.drop('Unnamed: 0', axis=1)





def change():

    sns.displot(data = df,x= 'SalePrice',height=6, aspect=2,bins=80,kde=True)
    plt.show()

#print(df[(df['SalePrice'] > 1600) & (df['SalePrice'] < 2100) & (df['TotRms AbvGrd'] > 7)][['Lot Area', 'TotRms AbvGrd', 'SalePrice']].head(30))
print(df.tail())