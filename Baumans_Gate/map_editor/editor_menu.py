from create_map import CreatorMap
from change_map import ChangeMap
import os
import logging


class Menu:
    def __init__(self):
        self.logger = logging.getLogger("map_editor") #Создается объект логгера с именем 'map_editor' для записи логов, связанных с редактором карт
        self.logger.setLevel(logging.DEBUG)
        self.handler = logging.FileHandler('map_log.txt', 'a', 'utf-8') #Создается обработчик логов self.handler, который будет записывать логи в файл map_log.txt
        self.formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.edit_process()
        self.status = 1
        self.list_of_maps = []

    def edit_process(self):
        self.list_of_maps = os.listdir('maps') #Получает список файлов в папке maps с помощью модуля os и сохраняет его в self.list_of_maps
        print("Добро пожаловать в редактор карт!")
        print(f"Существующие карты: {self.list_of_maps}")
        status = int(input("Выберите:\n"
                           "1 - создать карту\n"
                           "2 - изменить существующую карту\n"
                           "3 - удалить карту\n"
                           "0 - выйти из программы\n"))
        while status != 0:
            if status == 1:
                self.new_map = CreatorMap()
                self.logger.info(f"Создана карта {self.new_map.name}")
            elif status == 2:
                self.new_map = ChangeMap()
                self.logger.info(f"Изменена карта {self.new_map.chosen_map}")
            elif status == 3:
                self.delete_map()
            status = int(input("Выберите:\n"
                                "1 - создать карту\n"
                                "2 - изменить существующую карту\n"
                                "3 - удалить карту\n"
                                "0 - выйти из программы\n"))
            self.list_of_maps = os.listdir('maps') #обновляет список существующих карт
            print(f"Существующие карты: {self.list_of_maps}")

    def delete_map(self):
        name_map_delete = input("Введите название карты, которую хотие удалить: ")
        path = 'maps\\' + name_map_delete + '.txt' #формирует путь к файлу
        os.remove(path) #Удаляет файл карты с помощью модуля os.
        self.logger.info(f"Удалена карта {name_map_delete}")
