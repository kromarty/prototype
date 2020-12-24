class vehicle:
    def __init__(self, brand, model, color, type, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.type = type
        self.price = price

    def get_info(self):
        print("Марка: " + self.brand)
        print("Модель: " + self.model)
        print("Цвет: " + self.color)
        print("Тип кузова: " + self.type)
        print("Цена: " + str(self.price))
        print()