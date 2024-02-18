from .multi_functions import *
import pandas as pd

df = pd.read_csv(r"C:\Users\Ардак\Documents\Python machine learning\UNZIP_ME_FOR_NOTEBOOKS_ML_RUS_V6\DATA\new.csv")
df['SalePrice'] = df['SalePrice']//100
df = df.drop('Unnamed: 0', axis=1)

array = []

def registration():
    name = input("Name:  ")
    username = input("Username: ")
    email = input("email: ")
    phone_number = input("phone_number:  ")
    age = input("age:  ")
    login = (name,username,email,phone_number,age)
    print("Регистрация прошло успешно! \n"
          f"Имя пользователя: {name} {username}  \n"
          f"Возраст:  {age}  \n"
          f"Почта: {email}  \n"
          f"Номер телефона: {phone_number}  \n")
    right = input("Все правильно? Yes / No:  \n")
    if right=="No":
        print("Повторная регистрация:  \n")
        registration()
    elif right == "Yes":
        print("Пользователь сохранен успешно! ")





def catalog():
    print(df)
    print("Корзина : \n"
          "1.Добавить  \n"
          "2.Выйти \n")
    word = int(input("Выбрать: "))
    if word==1:
        n = int(input('Напишите номер товара: '))
        array.append(n)
        print("Товар добавлен в корзину *  \n")


def filter_():
    print("Выберите категорию:  \n"
          "1. Самые Популярные \n"
          "2.Самые Дешёвые  \n"
          "3.Самые Дорогие\n"
          "4.Выбрать по ценовым категориям \n"
          "5.Выйти  \n")

    choice = int(input("Ваш выбор: "))


    while True:
        if choice == 1:
            print(df.head(50))
            filter_()

            break

        elif choice == 2:
            print(df.nsmallest(50, 'SalePrice'))
            filter_()
            break

        elif choice == 3:
            print(df.nlargest(50, 'SalePrice'))
            filter_()
            break

        elif choice == 4:
            filter_money()
            break
        elif choice ==5:
            break




def top_50():
    print(df.nlargest(50, 'SalePrice'))
    print("Корзина : \n"
          "1.Добавить  \n"
          "2.Выйти \n")
    word = int(input("Выбрать: "))
    if word == 1:
        n = int(input('Напишите номер товара: '))
        array.append(n)
        print("Товар добавлен в корзину *  \n")



def upload_apartment(df):
    print("Заполните данные о вашей квартире.. \n")
    area = int(input('Площадь земли: '))
    year = int(input('Год Строение: '))
    bath = int(input('Количество ванные: '))
    bedroom = int(input('Количество спальни: '))
    kitchen = int(input('Количество кухни: '))
    total_room = int(input('Количество комнат: '))
    sale = int(input('Цена: '))

    apartment_data = {
        'Lot Area': [area],
        'Year Built': [year],
        'Full Bath': [bath],
        'Bedroom AbvGr': [bedroom],
        'Kitchen AbvGr': [kitchen],
        'TotRms AbvGrd': [total_room],
        'SalePrice': [sale]
    }


    apartment_df = pd.DataFrame(apartment_data)
    df = pd.concat([df, apartment_df], ignore_index=True)

    print("Данные о квартире успешно добавлены в каталог.  \n")





def average_price():
    change()







def my_apartment():
    print(df.tail(10))


def cart():
    for i in range(len(array)):
        print(f"{i+1} Квартира _ под номером {array[i]} \n")
        print(df.iloc[array[i]])
        print('\n')


def change_info_own_flat():
    change_info()


