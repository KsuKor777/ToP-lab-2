import random
import json


class CreatorMap:
    def __init__(self):
        print("Добро пожаловать в редактор карт!")
        self.field = []
        chose = int(input("1 - создать новое препятствие\n"
                          "2 - случайное создание карты из базовых препятствий\n"
                          "3 - создание карты из базовых препятствий\n"))
        self.new_symbols = {} #Инициализирует пустой словарь
        if chose == 1:
            self.set_new_obstacle()
        elif chose == 2:
            self.set_pr()
        elif chose == 3:
            self.create_base_field()
        print("Полученное поле:")
        self.display()
        self.name = 0
        self.saved = self.save_in_file()

    def set_pr(self):
        self.field = [['*' for i in range(15)] for i in range(15)]
        for i in range(1, 14):
            for j in range(15):
                if random.randint(0, 8) == 1:
                    self.field[i][j] = random.choice(['@', '#', '!'])

    def set_new_obstacle(self):
        self.field = [['*' for i in range(15)] for i in range(15)]
        flag_zero = 1 #Цикл добавления препятствий
        while flag_zero != 0:
            new_sym = input("Введите символ препятствия: ")
            if len(new_sym) != 1: #Проверяет, состоит ли введенный символ из одного символа. Если нет, то берет первый символ из введенной строки
                new_sym = new_sym[0]
            new_penalty = float(input("Введите, сколько очков перемещения необходимо для преодоления препятствия: "))
            self.new_symbols[new_sym] = new_penalty #Добавляет новый символ в словарь self.new_symbols с его штрафом за преодоление
            flag_zero = int(input("Символ добавлен\n"
                                  "0 - сохранение карты\n"
                                  "1 - добавить ещё одно препятствие\n"))
        for key in self.new_symbols.keys():#перебирает все символы в словаре self.new_symbols и вызывает self.set_sym_on_field(key) для размещения каждого символа на поле
            self.set_sym_on_field(key)

    def create_base_field(self):
        self.field = [['*' for i in range(15)] for i in range(15)]
        base_symbols = ['!', '#', '@']
        for sym in base_symbols: #Перебирает все символы из base_symbols и вызывает метод self.set_sym_on_field(sym) для размещения каждого символа на поле.
            self.set_sym_on_field(sym)

    def set_sym_on_field(self, sym):
        flg = 0
        while flg != 1:
            x = int(input(f"Введите кооринату X (до 14) для символа {sym}: "))
            y = int(input(f"Введите кооринату Y (до 14) для символа {sym}: "))
            if x < 15 and y <15:
                self.field[y][x] = sym #Устанавливает символ sym в соответствующую клетку поля.
            else:
                print("Нет такой клетки")
            flg = int(input('0 - добавить ещё один подобный символ на поле\n'
                            '1 - сохранить эти символы\n'))

    def display(self):
        for row in self.field:
            print(' '.join(row))

    def save_in_file(self): # Создает словарь data, который будет содержать информацию о карте для сохранения в файл.
   #'field': self.field: Сохраняет информацию о поле карты в виде двумерного списка self.field.
   # 'new_symbols': self.new_symbols: Сохраняет информацию о новых символах препятствий (их значения) в словаре self.new_symbols.
        self.name = input('Введите название сохранённого поля: ')
        data = {'field': self.field, 'new_symbols': self.new_symbols}
        with open(f"maps\\{self.name}.txt", 'w') as file:
            json.dump(data, file)
        return "карта создана"
