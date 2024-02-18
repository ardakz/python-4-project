import rent.functions as rent
import pandas as pd
df = pd.read_csv(r"C:\Users\Ардак\Documents\Python machine learning\UNZIP_ME_FOR_NOTEBOOKS_ML_RUS_V6\DATA\new.csv")
df['SalePrice'] = df['SalePrice']//100
df = df.drop('Unnamed: 0', axis=1)



def main_menu():
    while True:
        print("Выберите действие:\n"
              "1. Регистрация\n"
              "2. Каталог квартир для аренды\n"
              "3. Фильтр\n"
              "4. ТОП 50 квартир\n"
              "5. Выложить квартиру на аренду\n"
              "6. Посмотреть среднюю цену своей квартиры\n"
              "7. Расположение своей квартиры в каталоге\n"
              "8. Корзина\n"
              "9. Изменить инф. о моем квартире \n"
              "10.Выход \n")

        choice = int(input('Введите число (1-10):\n'))

        if choice == 1:
            rent.registration()
        elif choice == 2:
            rent.catalog()
        elif choice == 3:
            rent.filter_()
        elif choice == 4:
            rent.top_50()
        elif choice == 5:
            rent.upload_apartment(df)
        elif choice == 6:
            rent.average_price()
        elif choice == 7:
            rent.my_apartment()
        elif choice == 8:
            rent.cart()
        elif choice == 9:
            rent.change_info_own_flat()

        elif choice == 10:
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите число от 1 до 10.")


main_menu()
