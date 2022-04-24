# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data():
    def __init__(self, dat):
        self.dat=dat
    def __str__(self):
        return print('Введена дата ', self.dat)
    @classmethod
    def transf_to_number(cls, dat):
        dmy=dat.split('-')
        day=int(dmy[0])
        month=int(dmy[1])
        year=int(dmy[2])
        return print(day, month, year)
    @staticmethod
    def validation(day, month, year):
        if day<1 or day>31:
            print('Введите корректную дату')
        elif month<1 or month>12:
            print('Введите корректный номер месяца')
        elif year<1900 or year>2022:
            print('Введите корректный год')
        else:
            print("Все нормально")
a=Data("17-04-2022")
print(a.__str__())
b="17-04-2022"
print(Data.transf_to_number(b))
print (Data.validation(21, 4, 2022))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# # # Проверьте его работу на данных, вводимых пользователем.
# # При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class My_exception(Exception):
    def __init__(self, ex_text):
        self.ex_text = ex_text
inp_delimoe = float(input('Введите делимое: '))
inp_delitel = float(input('Введите делитель: '))
try:
    if inp_delitel==0:
        raise My_exception("Делитель не может равняться 0!")
except My_exception as message:
    print (message)
else:
    res=inp_delimoe/inp_delitel
    print(f'Получен результат: {res}')

# # 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# # Проверить работу исключения на реальном примере.
# # Запрашивать у пользователя данные и заполнять список необходимо только числами.
# # Класс-исключение должен контролировать типы данных элементов списка.
# # Примечание: длина списка не фиксирована.
# # Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
# # При этом скрипт завершается, сформированный список с числами выводится на экран.
# # Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# # Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# # Вносить его в список, только если введено число.
# # Класс-исключение должен не позволить пользователю ввести текст (не число)
# # и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class Check_For_Num_Error(Exception):
    def __init__(self, t):
        self.t=t
a=[]
while True:
    try:
        num_in_list=input('Введите число (либо введите stop для прекращения ввода): ')
        if num_in_list.isdigit() == True:
            a.append(int(num_in_list))
        elif num_in_list == 'stop':
            break
        elif num_in_list.isdigit() == False:
            raise Check_For_Num_Error('Вы ввели не число')
    except Check_For_Num_Error as err:
        print(err)
print(a)

# # 4. Начните работу над проектом «Склад оргтехники».
# # Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# # Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# # В базовом классе определите параметры, общие для приведённых типов.
# # В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# # 5. Продолжить работу над первым заданием.
# # Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# # Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# # можно использовать любую подходящую структуру (например, словарь).
# # 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# # Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# # Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
#

class Sklad:
    def __init__(self):
        self.on_sklad_dict = {}

    def add_to(self, orgtechnika):
        ''' добавляем в словарь обьект по его названию, в значении
        будет список экземпляров этого оборудования'''
        self.on_sklad_dict.setdefault(orgtechnika.group_name(), []).append(orgtechnika)

    def extract(self):
        self.unit=input("Какую технику передаем?")
        for k, v in self.on_sklad_dict.items():
            for i in v:
                if self.unit in i:
                    ind=v.index(i)
                    v.pop(ind)

class Orgtechnika:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'

class Printer(Orgtechnika):
    def __init__(self, name, make, year, type="лазерный"):
        super().__init__(name, make, year)
        self.type=type

    def __repr__(self):
        return f'{self.name} {self.type} {self.make} {self.year}'

class Scaner(Orgtechnika):
    def __init__(self, name, make, year, resolution= 1200):
        super().__init__(name, make, year)
        self.resolution=resolution

    def __repr__(self):
        return f'{self.name} {self.resolution} {self.make} {self.year}'

class Xerox(Orgtechnika):
    def __init__(self,  name, make, year, productivity=10000):
        super().__init__(name, make, year)
        self.productivity=productivity

    def __repr__(self):
        return f'{self.name} {self.productivity} {self.make} {self.year}'
sklad=Sklad()
printer = Printer("HP-880", "HP", 2021)
sklad.add_to(printer)
scaner = Scaner("Sony-113", "Sony", 2022)
sklad.add_to(scaner)
xerox = Xerox("15502E", "Xerox", 2021)
sklad.add_to(xerox)
printer = Printer("HP-480", "HP", 2022, "струйный")
sklad.add_to(printer)
scaner = Scaner("HP-0808", "HP", 2022, 600)
sklad.add_to(scaner)
xerox = Xerox("HP-9895A", "HP", 2021, 20000)
sklad.add_to(xerox)
print(f'На складе: {sklad.on_sklad_dict}')
sklad.extract()
print (f'На складе: {sklad.on_sklad_dict}')


# # 7. Реализовать проект «Операции с комплексными числами».
# # Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# # Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# # сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexN:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма a и b равна')
        return f' {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение a и b равно')
        return f' {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

z_1 = ComplexN (1, -2)
z_2 = ComplexN(3, 4)

print(z_1 + z_2)
print(z_1 * z_2)