# Создать классTrafficLight(светофор).
# # определить у него один атрибутcolor(цвет) и методrunning(запуск);
# # атрибут реализовать как приватный;
# # в рамках метода реализовать переключение светофора в режимы:красный,жёлтый, зелёный;
# # продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# # третьего (зелёный) — на ваше усмотрение;
# # переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# # проверить работу примера, создав экземпляр и вызвав описанный метод.
# # Задачу можно усложнить, реализовав проверку порядка режимов.
# # При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
class TrafficLight():
    __color = {'красный': 7, 'желтый': 2, 'зеленый': 4}
    def running(self):
        while True:
            for c, tm in self.__color.items():
                print(c)
                self.t = time.sleep(tm)
svetofor = TrafficLight()
print(svetofor.running())
#
# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного
# кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road():
    def __init__(self, _length, _width):
        self._length=_length
        self._width=_width

    def calc (self,th):
        self.th=th
        return 25*self._length*self._width*self.th
m = Road(20,20)
print(f'Масса асфальта для покрытия всей дороги составляет {m.calc(2)} тонн')

#
# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker():
     def __init__(self, name, surname, position, wage, bonus):
         self.name=name
         self.surname = surname
         self.position= position
         self._income = {"wage":wage, "bonus":bonus}
class Positions(Worker):
    def get_full_name(self):
        return self.name + ' '+ self.surname
    def get_total_income(self):
        return self._income.get("wage")+self._income.get('bonus')
a = Positions ('Петр', 'Петров', 'кладовщик', 2500, 2000)
print(a.get_full_name())
print(a.get_total_income())

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
#
class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed=speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        if self.speed>0:
            print("Машина поехала")
    def stop(self):
        if self.speed ==0:
            print('Машина остановилась')
    def turn(self, direction):
        self.direction = direction
        print('Машина повернула ',self.direction)
    def show_speed(self):
        print('Текущая скорость', self.speed)
class TownCar(Car):
    def show_speed(self):
        print("Текущая скорость", self.speed)
        if self.speed>60:
            print('Превышение скорости')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        print("Текущая скорость", self.speed)
        if self.speed > 40:
            print('Превышение скорости')
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

ferrari = SportCar(100, 'красный', 'Ferrari', False)
logan = TownCar(30, 'белый', 'Logan', False)
ford = WorkCar(70, 'розовый', 'Ford', True)
skoda = PoliceCar(110, 'синий',  'Scoda', True)
print(ferrari.turn("налево"))
print(ford.turn('направо'))
print(ferrari.stop())
print(ford.go())
print(ford.show_speed())
print(f'{skoda.name} - {skoda.color} автомобиль')
print(f'{skoda.name} - полицейская машина? {skoda.is_police}')
print(f'{logan.name}  - полицейская машина? {logan.is_police}')
print(logan.show_speed())
print(ferrari.show_speed())
print(skoda.show_speed())

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')
class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')
a=Stationery("Пишущий предмет")
a.draw()
b=Pen('Пищущий предмет')
b.draw()
c = Pencil('Пищущий предмет')
c.draw()
d=Handle('Пищущий предмет')
d.draw()





