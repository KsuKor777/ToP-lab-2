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

def test_buy():
    fake_inputs = [
        '0',
        'ksusha',
        '1234',
        '3',
        '2',
        'map',
        '1',
        '20',
        'Лучник',
        'Лучник',
        '3'
    ]
    with patch('builtins.input', side_effect=fake_inputs):
        game = GameMenu()
        logger.info("Тест покупки юнитов успешно выполнен")
    assert game.units != 0
