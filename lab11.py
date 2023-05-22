'''Задача «Ресторан»: создайте класс с именем Restaurant.
Метод __init__() класса Restaurant должен содержать два атрибута:
restaurant_name (название ресторана) и cuisine_type (тип кухни).
Создайте метод describe_restaurant(), который выводит два атрибута,
и метод open_restaurant(), который выводит сообщение о том, что ресторан открыт.
Создайте на основе своего класса экземпляр с именем newRestaurant.
Выведите два атрибута по отдельности, затем вызовите оба метода.'''

def lab1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название Ресторана {self.restaurant_name},  кухня: {self.cuisine_type} русская.")

        def open_restaurant(self):
            print("Ресторан сейчас открыт.")

    newRestaurant = Restaurant("Myrka", "")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

'''На основе ранее созданного класса Restaurant из задания 11.1 
создайте три разных экземпляра (три ресторана), вызовите для каждого экземпляра метод describe_restaurant().'''

def lab2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name} Кухня: {self.cuisine_type}.")

        def open_restaurant(self):
            print("Ресторан сейчас открыт")

        # Создаем три экземпляра класса Restaurant

    restaurant1 = Restaurant("Myrka", "Русская")
    restaurant2 = Restaurant("Pepperoni", "Итальянская")
    restaurant3 = Restaurant("Onigiri", "Японская")

    # Вызываем метод describe_restaurant() для каждого экземпляра
    restaurant1.describe_restaurant()
    restaurant2.describe_restaurant()
    restaurant3.describe_restaurant()

'''Добавьте в созданный класс Restaurant атрибут, 
задающий начальный рейтинг ресторана и метод, 
который получает на вход новое значение рейтинга и обновляет его.'''

def lab3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, initial_rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = initial_rating

        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}кухня: {self.cuisine_type}  русская .")

        def open_restaurant(self):
            print("Ресторан сейчас открыт.")

        def update_rating(self, new_rating):
            self.rating = new_rating
            print(f"Рейтинг ресторана {self.restaurant_name} Был обновлен до  {self.rating}.")

        # Создаем экземпляр класса Restaurant с начальным рейтингом

    restaurant1 = Restaurant("Myrka", "Русская", 3)

    # Выводим текущий рейтинг ресторана
    print(f"Изначальынй рейтинг ресторана {restaurant1.restaurant_name}   {restaurant1.rating} .")

    # Обновляем рейтинг и выводим новое значение
    restaurant1.update_rating(5)
    print(f"Новый, обновленный рейтинг  {restaurant1.restaurant_name} : {restaurant1.rating}.")


lab1()
lab2()
lab3()