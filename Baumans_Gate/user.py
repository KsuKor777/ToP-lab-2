import pickle
from town.building import DoctorHouse, Arsenal, Forge, Market, Tavern, Workshop, Academy


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.wallet = {}
        self.buildings = {'doctor_house': DoctorHouse(), 'forge': Forge(), 'arsenal': Arsenal(), 'market': Market(),
                          'tavern': Tavern(), 'workshop': Workshop(), 'academy': Academy()} #Создает словарь self.buildings, содержащий объекты различных зданий. Каждое здание инициализируется с использованием соответствующего класса
        self.new_unit = 0

    # Каждый метод buy_* предназначен для покупки соответствующего здания. Внутри этих методов происходит вызов метода buying соответствующего здания
    def buy_doctors_house(self):
        self.buildings['doctor_house'].buying(self)

    def buy_forge(self):
        self.buildings['forge'].buying(self)

    def buy_arsenal(self):
        self.buildings['arsenal'].buying(self)

    def buy_tavern(self):
        self.buildings['tavern'].buying(self)

    def buy_market(self):
        self.buildings['market'].buying(self)

    def buy_workshop(self):
        if self.buildings['workshop'].status == 0:
            self.buildings['workshop'].buying(self)
        else:
            self.buildings['workshop'].upgrade(self)

    def buy_academy(self):
        self.buildings['academy'].buying(self)

    def getting_buffs(self, units):
        for unit in units: #Начинает цикл, который проходит по каждому юниту в списке units.
            for item in self.buildings.values(): #проход по всем зданиям, представленным в self.buildings. Используется метод .values()
                if item.status == 1 and item.parameter != 0:
                    unit.params[item.parameter] += item.boost #Обращается к параметрам конкретного юнита и выбирает тот параметр, который соответствует item.parameter. Добавляет значение буста, которое связано с активным зданием, к этому параметру юнита

    def save(self):
        self.new_unit = self.buildings['academy'].new_unit
        with open(f'users\\{self.name}.pickle', 'wb') as f:
            pickle.dump(self, f)
