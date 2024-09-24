from unittest.mock import patch
from menu import GameMenu
import logging
import pytest

# получим логгер для нашего приложения либо создадим новый, если он еще не создан
logger = logging.getLogger("tests") #создает объект логгера с именем "tests"
logger.setLevel(logging.DEBUG) #Устанавливает уровень логирования для логгера.  logging.DEBUG означает, что будут записываться все сообщения с уровнем DEBUG и выше (например, INFO, WARNING, ERROR, CRITICAL).
# опишем, куда и как будем сохранять логи: зададим файл и формат
handler = logging.FileHandler('test_log.txt', 'a', 'utf-8') #logging.FileHandler — это класс, отвечающий за запись логов в файл.
formatter = logging.Formatter("%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s") #logging.Formatter — это класс, отвечающий за форматирование сообщений логов.   - %(filename)s: Имя файла, где произошла ошибка.
#[LINE:%(lineno)d]: Номер строки, где произошла ошибка.
# %(levelname)-8s: Уровень логирования (например, "DEBUG", "INFO", "ERROR").
# [%(asctime)s]: Текущая дата и время.
# %(message)s: Сообщение лога.

# установим файлу нужный формат, а нужный файл - логгеру
handler.setFormatter(formatter) #все логи, которые будут записываться обработчиком handler, будут форматироваться согласно заданному формату
logger.addHandler(handler) #все логи, которые будут генерироваться логгером logger, будут переданы обработчику handler для записи в файл.

def test_cost():
    fake_inputs = [
        '0',
        'ksusha',
        '1234',
        '3',
        '2',
        'map',
        'test',
        'Test',
        '3',
        '0',
        '0',
        '2'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.test_cost()
        logger.info("Тест прочсёта штрафа успешно выполнен")
    assert game.costing == "Недостаточно очков для перемещения"


def test_attack():
    fake_inputs = [
        '0',
        'ksusha',
        '1234',
        '3',
        '2',
        'map',
        '0',
        'test',
        '3',
        '0',
        'да'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.test_attack()
        logger.info("Тест проведения атаки успешно выполнен")
    assert game.costing == "Вражеский боец был атакован"


def test_walk():
    fake_inputs = [
        '0',
        'ksusha',
        '1234',
        '3',
        '2',
        'map',
        'test',
        'Test',
        '0',
        '0',
        'X',
        '-1'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.test_cost()
        logger.info("Тест проведения ходьбы успешно выполнен")
    assert game.costing == 'Не выходите за карту'


def test_death():
    fake_inputs = [
        '0',
        'ksusha',
        '1234',
        '3',
        '2',
        'map',
        '1',
        'test',
        '3',
        '0',
        'да',
        '0',
        'да'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        death = game.test_death()
        logger.info("Тест смерти успешно выполнен")
    assert death == 0
