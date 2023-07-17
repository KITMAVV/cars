print("1 - почати")


class auto():
    def add(self, model, year, engine, color, price):
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
        self.price = price
    def print_(self):
        print(f'Модель {self.model}, {self.year} року випуску з об’ємом двигуна {self.engine} літрів, коліру {self.color} та вартістю {self.price} доларів')
    def change_model(self, new_model):
        self.model = new_model
    def change_year(self, new_year):
        self.year = new_year
    def change_engine(self, new_engine):
        self.engine = new_engine
    def change_color(self, new_color):
        self.color = new_color
    def change_price(self, new_price):
        self.price = new_price
    def __gt__(self, next):
        if self.price > next.price:
            return True
        else:
            return False
    def __lt__(self, next):
        if self.year < next.year:
            return True
        else:
            return False
    def __eq__(self, next):
        if self.engine == next.engine:
            return True
        else:
            return False

pa = auto()
pa2 = auto()
while True:

    a = int(input("Введіть сюди: "))
    if a == 1:
        pa.change_model(input("Введіть модель: "))
        pa.change_year(int(input("Введіть рік(тільки цифри): ")))
        pa.change_engine(int(input("Введіть об’єм двигуна(тільки цифри): ")))
        pa.change_color(input("Введіть колір: "))
        pa.change_price(int(input("Введіть ціну(тільки цифри): ")))
        print("Тепер введіть про другу машинку:")
        pa2.change_model(input("Введіть модель: "))
        pa2.change_year(int(input("Введіть рік(тільки цифри): ")))
        pa2.change_engine(int(input("Введіть об’єм двигуна(тільки цифри): ")))
        pa2.change_color(input("Введіть колір: "))
        pa2.change_price(int(input("Введіть ціну(тільки цифри): ")))
        pa.print_()
        pa2.print_()
        print("     1 - почати заново", " ", "2 - змінити модель", " ", "3 - змінити рік", " ", "4 - змінити об’єм", " ", "5 - змінити колір", " ", " 6 - змінити ціну", " ", "7 - порівняти", " ", "8 - допобачення")
    if a == 2:
        pa.change_model(input("Введіть модель першої машини: "))
        pa2.change_model(input("Введіть модель другої машини: "))
        pa.print_()
        pa2.print_()
        print("     1 - почати заново", " ", "2 - змінити модель", " ", "3 - змінити рік", " ", "4 - змінити об’єм", " ", "5 - змінити колір", " ", " 6 - змінити ціну", " ", "7 - порівняти", " ", "8 - допобачення")
    if a == 3:
        pa.change_year(int(input("Введіть рік першої машини(тільки цифри): ")))
        pa2.change_year(int(input("Введіть рік другої машини(тільки цифри): ")))
        pa.print_()
        pa2.print_()
        print("     1 - почати заново", " ", "2 - змінити модель", " ", "3 - змінити рік", " ", "4 - змінити об’єм", " ", "5 - змінити колір", " ", " 6 - змінити ціну", " ", "7 - порівняти", " ", "8 - допобачення")
    if a == 4:
        pa.change_engine(int(input("Введіть об’єм двигуна першої машини(тільки цифри): ")))
        pa2.change_engine(int(input("Введіть об’єм двигуна другої машини(тільки цифри): ")))
        pa.print_()
        pa2.print_()
        print("     1 - почати заново", " ", "2 - змінити модель", " ", "3 - змінити рік", " ", "4 - змінити об’єм", " ", "5 - змінити колір", " ", " 6 - змінити ціну", " ", "7 - порівняти", " ", "8 - допобачення")
    if a == 5:
        pa.change_color(input("Введіть колір першої машини: "))
        pa2.change_color(input("Введіть колір другої машини: "))
        pa.print_()
        pa2.print_()
        print("     1 - почати заново", " ", "2 - змінити модель", " ", "3 - змінити рік", " ", "4 - змінити об’єм", " ", "5 - змінити колір", " ", " 6 - змінити ціну", " ", "7 - порівняти", " ", "8 - допобачення")
    if a == 6:
        pa.change_price(int(input("Введіть ціну першої машини(тільки цифри): ")))
        pa2.change_price(int(input("Введіть ціну другої машини(тільки цифри): ")))
        pa.print_()
        pa2.print_()
        print("     1 - почати заново", " ", "2 - змінити модель", " ", "3 - змінити рік", " ", "4 - змінити об’єм", " ", "5 - змінити колір", " ", " 6 - змінити ціну", " ", "7 - порівняти", " ", "8 - допобачення")

    if a == 7:
        if pa > pa2:
            print("Перший дорожчий")
        else:
            print("Другий дорожчий")

        if pa < pa2:
            print("Перший старший")
        else:
            print("Другий старший")

        if pa == pa2:
            print("Двигуни однакові")
        else:
            print("Двигуни різні")
        print("     1 - почати заново", " ", "2 - змінити модель", " ", "3 - змінити рік", " ", "4 - змінити об’єм", " ", "5 - змінити колір", " ", " 6 - змінити ціну", " ", "7 - порівняти", " ", "8 - допобачення")
    if a == 8:
        print("Допобачення!!!")
        break
    #Пробачте що таке довге...                                                  Послідовність перевірки завдяння: 1 => ввести данні => 7 => 8
    #(тільки цифри) - це нагадування, бо я путався коли швидко перевіряв