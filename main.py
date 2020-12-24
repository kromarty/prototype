from vehicle import vehicle
from supply import supply
from order import order
from warehouse import warehouse
from client import client
from supplier import supplier
import numpy as np
import re

wh = warehouse()

option = None
print("Добро пожаловать на Buybuycar, укажите, вы хотите купить или продать автомобиль?")
while option != 0:
    print("1. Купить")
    print("2. Продать")
    print("0. Выйти ")
    option = input()
    while option != '1' and option != '2' and option != '0':
        option = input("Повторите ввод: ")

    option = int(option)

    if option == 1:
        ord = order()
        opt = ""
        vs = list(wh.vehicles.keys())
        while opt != 'n' and len(vs) != 0:
            print("Список доступных автомобилей:")
            cnt = 0
            for v in vs:
                cnt += 1
                print(str(cnt))
                v.get_info()
                print()
            n = input("Введите номер автомобиля (0 чтобы выйти):")
            while not re.fullmatch("[+]?\d+", n):
                n = input("Введите целое неотрицательное число")
                if re.fullmatch("[+]?\d+", n):
                    if int(n) > len(list(wh.vehicles.values())):
                        n = ""

            n = int(n)
            if n > 0:
                ord.AddVehicle(vs[n - 1])
                del vs[n - 1]
                opt = input("Желаете выбрать ещё автомобиль? [y/n]")
                while opt != 'y' and opt != 'n':
                    opt = input()
            else:
                break
        if ord.Cost() > 0:
            fio = input("Ваше ФИО: ")
            cl = client(fio)
            opt = input("Желаете заказать доставку? [y/n]")
            while opt != 'y' and opt != 'n':
                opt = input()
            if opt == 'y':
                address = input("Введите адрес доставки")
                ord.SetDeliveryAddress(address)
            print("Общая стоимость: " + str(ord.Cost()))
            opt = input("Подтвердите заказ [y/n]")
            while opt != 'y' and opt != 'n':
                opt = input()
            if opt == 'y':
                print("Подтверждено.")
                for v in ord.vehicles:
                    wh.places.append(wh.vehicles[v])
                    del wh.vehicles[v]
            else:
                print("Отмена операции")


    elif option == 2:
        n = input("Введите количество автомобилей:")
        while not re.fullmatch("[+]?\d+", n):
            n = input("Введите целое положительное число")
        n = int(n)
        if n > len(wh.places):
            print("Недостаточно места")
        else:
            prov = input("Введите название своей компании: ")
            supler = supplier(prov)
            sup = supply(prov)
            for i in range(n):
                print("Введите параметры автомобиля:")
                brand = input("Марка: ")
                model = input("Модель: ")
                color = input("Цвет: ")
                type = input("Тип кузова: ")
                price = int(input("Цена: "))
                sup.AddVehicle(vehicle(brand, model, color, type, price))
            print("Ваши тс:")
            sup.GetProducts()
            opt = input("Подтвердите поставку [y/n]")
            while opt != 'y' and opt != 'n':
                opt = input()
            if opt == 'y':
                print("Подтверждено. Доставьте автомобили по адресу ул. Пушкина, д. 17")
                for v in sup.vehicles:
                    wh.vehicles[v] = wh.places[0]
                    del wh.places[0]
            else:
                print("Отмена операции")

np.save('database.npy', wh.vehicles)
np.save('places.npy', wh.places)