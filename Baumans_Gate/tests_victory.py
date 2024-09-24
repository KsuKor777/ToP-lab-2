from linecache import cache
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

# тест 1
def test_player():
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
        'да',
    ]
    with patch('builtins.input', side_effect=fake_inputs): #Использует контекстный менеджер patch из unittest.mock, чтобы заменять стандартную функцию input на свою реализацию, которая будет возвращать значения из списка fake_inputs.

        try:
            game = GameMenu()
            game.game_process()
            logger.info("Тест победы игрока прошел успешно")
        except Exception as e:
            logger.info("Тест победы игрока не выполнен")
            raise e
    assert game.result == "---------------Вы победили------------------\n" #Использует утверждение assert для проверки, что атрибут game.result равен ожидаемому значению .


# тест 2
def test_bot():
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
        '0'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        game.game_process()
        logger.info("Тест победы бота успешно выполнен")
    assert game.result == "---------------Вы проиграли------------------\n"
